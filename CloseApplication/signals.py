from django.conf import settings
from django.db.models.signals import pre_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import TaskChecklist, subTaskChecklist, AccountReconciliationList
from datetime import datetime
from notifications.signals import notify

#signal logic -- if subtask status change, check if all subtasks completed, if so generate
#parent task and associated subtasks (not need to confirm not exists before creation)
def Roll_Year(month, occurence):
    if occurence == "M":
        try:
            if (month + 1) > 12:
                return 1
            else:
                return 0
        except:
            return "Month Error"
    if occurence == "Q":
        try:
            if (month + 3) > 12:
                return 1
            else:
                return 0
        except:
            return "Quarterly Error"
    if occurence == "S":
        try:
            if(month + 6) > 12:
                return 1
            else:
                return 0
        except: 
            return "Semi-Annual Error"
    if occurence == "A":
        return 1

def Roll_Month(month, occurence):
    try:
        if occurence == "M":
            try:
                if (month + 1) > 12:
                    return (month + 1) - 12
                else:
                    return month + 1
            except:
                return "Month Error"
        if occurence == "Q":
            try:
                if (month + 3) > 12:
                    return (month + 3) - 12
                else:
                    return month + 3
            except:
                return "Quarterly Error"
        if occurence == "S":
            try:
                if(month + 6) > 12:
                    return (month + 6) - 12
                else:
                    return month + 6
            except: 
                return "Semi-Annual Error"
        if occurence == "A":
            return month
    except:
        return "No occurence found"
    
    


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

@receiver(pre_save, sender=AccountReconciliationList)
def notifications_AccountReconciliationList(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        reconciliationOwnerId_Previous = obj.reconciliationOwnerId 
        reconciliationOwnerId_New = instance.reconciliationOwnerId

        if not reconciliationOwnerId_Previous == reconciliationOwnerId_New:
            notify.send(instance.reconciliationOwnerId, recipient=instance.reconciliationOwnerId, verb='Account reconciliation XYZ has been assigned to you for MM-YYYY')

@receiver(pre_save, sender=TaskChecklist)
def notifications_TaskChecklist(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        taskDescription_Previous = obj.taskDescription 
        taskDescription_New = instance.taskDescription
        
        dueMonthDay_Previous = obj.dueMonthDay
        dueMonthDay_New = instance.dueMonthDay
        owner_Previous = obj.taskOwnerId
        owner_New = instance.taskOwnerId
        
        if not owner_Previous == owner_New:
            notify.send(instance.taskOwnerId, recipient=instance.taskOwnerId, verb='Task' + str(instance.__str__) + 'was assigned to you.')
        if not dueMonthDay_Previous == dueMonthDay_New:
            notify.send(instance.taskOwnerId, recipient=instance.taskOwnerId, verb='Task' + str(instance.__str__) + 'has changed due dates from month day ' + str(dueMonthDay_Previous) + ' to ' + str(dueMonthDay_New))
        if not taskDescription_Previous == taskDescription_New:
            notify.send(instance.taskOwnerId, recipient=instance.taskOwnerId, verb='Task' + str(instance.__str__) + 'has changed descriptions.')

@receiver(pre_save, sender=subTaskChecklist)
def do_something_if_changed(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass # Object is new, so field hasn't technically changed, but you may want to do something else here.
    else:
        previous_Value = obj.subTaskStatus
        new_Value = instance.subTaskStatus
        print(sender.objects.all().filter(taskId=instance.taskId).all()[0].subTaskDescription)
        if not previous_Value == new_Value: # Field has changed
            print("Field has changed from " + str(previous_Value) + " to " + str(new_Value))
            if str(new_Value) == "CT" and instance.Not_Equal_CT == 1: #if equal to 1 on pre_save indicates 0 after save, thus all subtasks for associated parent task are completed and a rollover is required. 
                print(instance.Not_Equal_CT) 
                relatedTaskChecklistId = TaskChecklist.objects.all().get(pk=instance.Related_Task_PK).taskId #Related_Task_PK return the subtasks related parent task primary key 
                next_Task = TaskChecklist.objects.all().filter(taskId=relatedTaskChecklistId, entity=instance.Sub_Task_Entity, taskYear=instance.Sub_Task_Year + Roll_Year(instance.Sub_Task_Period, instance.Sub_Task_Occurence), taskPeriod=Roll_Month(instance.Sub_Task_Period, instance.Sub_Task_Occurence))
                if next_Task.exists():
                    return "Exists -- don't create a new task"
                else:
                    #Note: Consider creating the rollover task owner as  determined by who actually completed the task vs. the owner the task
                    create_Task = TaskChecklist(taskId=relatedTaskChecklistId,taskTBMapping=instance.Sub_Task_TBMapping,taskDescription=instance.Sub_Task_Description,taskYear=instance.Sub_Task_Year + Roll_Year(instance.Sub_Task_Period, instance.Sub_Task_Occurence),dueMonthDay=instance.Sub_dueMonthDay,taskPeriod=Roll_Month(instance.Sub_Task_Period, instance.Sub_Task_Occurence),taskOccurence=instance.Sub_Task_Occurence,taskOwnerId=instance.Sub_Task_OwnerId,isJE=instance.Sub_Task_IsJE,pub_date=datetime.now(),due_date=datetime.now(),entity=instance.Sub_Task_Entity)
                    create_Task.save()
                    associated_Subtasks = sender.objects.all().filter(taskId=instance.taskId).all()
                    notify.send(instance.Sub_Task_OwnerId, recipient=instance.Sub_Task_OwnerId, verb='New task was created')
                    for subTask in associated_Subtasks:
                        print(next_Task)
                        next_TaskGet = TaskChecklist.objects.all().get(taskId=relatedTaskChecklistId, entity=instance.Sub_Task_Entity, taskYear=instance.Sub_Task_Year + Roll_Year(instance.Sub_Task_Period, instance.Sub_Task_Occurence), taskPeriod=Roll_Month(instance.Sub_Task_Period, instance.Sub_Task_Occurence))
                        create_SubTask = subTaskChecklist(taskId=next_TaskGet, subTaskNumber=subTask.subTaskNumber, subTaskDescription=subTask.subTaskDescription, subTaskStatus="NS")
                        create_SubTask.save()

                                        #note to self, watch out for case where not completed = 0, but no associated subtasks