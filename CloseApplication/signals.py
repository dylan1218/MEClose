from django.conf import settings
from django.db.models.signals import pre_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import TaskChecklist, subTaskChecklist
from datetime import datetime

#signal logic -- if subtask status change, check if all subtasks completed, if so generate
#parent task and associated subtasks (not need to confirm not exists before creation)
def Roll_Month(month): #note, this doesn't consider reocurrence -- assumes monthly for testing purposes, will need to fix
    try:
        if month < 11 and month > 0:
            return month + 1
        elif month == 12:
            return 1
        elif month == 0:
            return "Month can't be 0"
    except:
        return "error"

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

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
                next_Task = TaskChecklist.objects.all().filter(taskId=relatedTaskChecklistId, entity=instance.Sub_Task_Entity, taskYear=instance.Sub_Task_Year, taskPeriod=Roll_Month(instance.Sub_Task_Period))
                if next_Task.exists():
                    return "Exists -- don't create a new task"
                else:
                    #Note: Consider creating the rollover task owner as  determined by who actually completed the task vs. the owner the task
                    create_Task = TaskChecklist(taskId=relatedTaskChecklistId,taskTBMapping=instance.Sub_Task_TBMapping,taskDescription=instance.Sub_Task_Description,taskYear=instance.Sub_Task_Year,taskPeriod=Roll_Month(instance.Sub_Task_Period),taskOccurence=instance.Sub_Task_Occurence,taskOwnerId=instance.Sub_Task_OwnerId,isJE=instance.Sub_Task_IsJE,pub_date=datetime.now(),due_date=datetime.now(),entity=instance.Sub_Task_Entity)
                    create_Task.save()
                    associated_Subtasks = sender.objects.all().filter(taskId=instance.taskId).all()
                    for subTask in associated_Subtasks:
                        print(next_Task)
                        next_TaskGet = TaskChecklist.objects.all().get(taskId=relatedTaskChecklistId, entity=instance.Sub_Task_Entity, taskYear=instance.Sub_Task_Year, taskPeriod=Roll_Month(instance.Sub_Task_Period))
                        create_SubTask = subTaskChecklist(taskId=next_TaskGet, subTaskNumber=subTask.subTaskNumber, subTaskDescription=subTask.subTaskDescription, subTaskStatus="NS")
                        create_SubTask.save()

                                        #note to self, watch out for case where not completed = 0, but no associated subtasks