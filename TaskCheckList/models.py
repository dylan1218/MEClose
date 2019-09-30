from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
import os
import datetime
from pandas.tseries.offsets import BDay
import calendar
import pandas as pd
#MEClose imports
from CompanyMaintain.models import userDefinedEntity
from CompanyMaintain.choices import periodChoices, statusChoices, binaryChoice


class TaskChecklist(models.Model):
    
    occurenceChoices = (
        ('M', 'Monthly'),
        ('Q', 'Quarterly'),
        ('S', 'Semi-Annually'),
        ('A', 'Annually'), 
    )
    
    taskId = models.CharField(max_length=8)
    taskTBMapping = models.CharField(max_length=200, default="Not Assigned") #For assigning tasks to a TB FSLI
    taskDescription = models.CharField(max_length=200)
    taskYear = models.IntegerField(max_length=4) 
    taskPeriod = models.IntegerField(max_length=2, choices = periodChoices)
    taskOccurence = models.CharField(max_length=2, choices = occurenceChoices)
    taskOwnerId = models.ForeignKey(User, on_delete=models.PROTECT) #For documentation purposes we want to preserve who the owner of a task was, and as such protect is utilized to not allow deletion of the referenced object
    isJE = models.CharField(max_length=3, choices=binaryChoice)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateField(("Due Date"), default=datetime.date.today) #Note: No longer needed -- will be a calculated property
    dueMonthDay = models.IntegerField(max_length=2, default=1)
    entity = models.ForeignKey(userDefinedEntity, on_delete=models.PROTECT, related_name="entity_TaskChecklist", default=1)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['taskId', 'entity', 'taskPeriod', 'taskYear'], name='unique_EntityUser')
        ]
    @property
    def Due_Date(self):
        dateStart = datetime.date(self.taskYear,self.taskPeriod, 1)
        dateEnd = datetime.date(self.taskYear, self.taskPeriod, calendar.monthrange(self.taskYear,self.taskPeriod)[1])
        firstBusinessDay = pd.date_range(dateStart, dateEnd, freq="BMS")
        return (firstBusinessDay + BDay(self.dueMonthDay-1)).date[0]


    @property
    def Not_Equal_CT(self):
        try:
            related_SubTask_Model = TaskChecklist.objects.prefetch_related("taskId_taskId").all().filter(taskId=self.taskId, entity=self.entity, taskPeriod=self.taskPeriod, taskYear=self.taskYear)
            related_SubTask_Model_Groupby = related_SubTask_Model[0].taskId_taskId.all().values("subTaskStatus").annotate(Count("subTaskStatus"))
            not_Completed_List = list(related_SubTask_Model_Groupby.exclude(subTaskStatus="CT").values_list("subTaskStatus__count", flat=True))
            return sum(not_Completed_List)
        except:
            return "error" #to work on except logic

    @property
    def aggregateStatus(self):
        try:
            related_SubTask_Model = TaskChecklist.objects.prefetch_related("taskId_taskId").all().filter(taskId=self.taskId, entity=self.entity, taskPeriod=self.taskPeriod, taskYear=self.taskYear)
            related_SubTask_Model_Groupby = related_SubTask_Model[0].taskId_taskId.all().values("subTaskStatus").annotate(Count("subTaskStatus")) #-1 to bring pk down relative to 0th based index
            
            not_Started_List = list(related_SubTask_Model_Groupby.filter(subTaskStatus="NS").values_list("subTaskStatus__count", flat=True))
            in_Progress_List = list(related_SubTask_Model_Groupby.filter(subTaskStatus="IP").values_list("subTaskStatus__count", flat=True))
            completed_List = list(related_SubTask_Model_Groupby.filter(subTaskStatus="CT").values_list("subTaskStatus__count", flat=True))

            #conditions to set status count for each status classification
            if len(not_Started_List) > 0:
                not_Started_Count = not_Started_List[0]
            else:
                not_Started_Count = 0
            
            if len(in_Progress_List) > 0:
                in_Progress_Count = in_Progress_List[0]
            else:
                in_Progress_Count = 0
            
            if len(completed_List) > 0:
                completed_Count = completed_List[0]
            else:
                completed_Count = 0

            if ( (not_Started_Count + in_Progress_Count + completed_Count) == 0 ) or ( (not_Started_Count > 0) and ((in_Progress_Count + completed_Count) == 0) ) :
                return "Not Started"
            elif in_Progress_Count > 0:
                return "In Progress"
            else:
                return "Completed"
        except:
            return "Unable to calculate status"

        
    @property #@property decorater utilized to create a callable calculated "field" similar to other fields
    def taskIdKey(self):
        return str(self.entity) + "-" + str(self.taskId) + "-" + str(self.taskYear) + "-" + str(self.taskPeriod)

    def __str__(self):
        return str(self.entity) + "-" + str(self.taskId) + "-" + str(self.taskYear) + "-" + str(self.taskPeriod)
#Note: need to revaluate foreign key within subtaskchecklist -- might need to append taskId     +Entity+Year+Period for a unique key
class subTaskChecklist(models.Model):
    taskId = models.ForeignKey(TaskChecklist, related_name="taskId_taskId", on_delete=models.CASCADE) #this field is our associated between the parent task and subtask(s). Cascade is utilize to remove the subtasks if parent task is removed
    subTaskNumber = models.IntegerField(max_length=2, default=1) #Maximum number of subtasks set to 99
    subTaskDescription = models.CharField(max_length=200)
    subTaskStatus = models.CharField(max_length=2, choices = statusChoices)
    #Note I did not add additional fields as the related parent should contain this data 
    #unique contrain entity, taskId, subTaskNumber, year, period
    #Note that taskId __str__ method returns the entity, taskId, taskYear and taskPeriod
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['taskId', 'subTaskNumber'], name='unique_Subtask')
        ]
    #The properties listed below return data from the associated parent task. 
    @property
    def Sub_dueMonthDay(self):
        related_dueMonthDay = subTaskChecklist.objects.all().get(id=self.id).taskId.dueMonthDay
        return related_dueMonthDay
    @property
    def Sub_Task_Year(self):
        related_Year = subTaskChecklist.objects.all().get(id=self.id).taskId.taskYear
        return related_Year
    @property
    def Sub_Task_Period(self):
        related_Period = subTaskChecklist.objects.all().get(id=self.id).taskId.taskPeriod
        return related_Period
    @property
    def Sub_Task_Entity(self):
        related_Entity = subTaskChecklist.objects.all().get(id=self.id).taskId.entity
        return related_Entity
    @property
    def Sub_Task_TBMapping(self):
        related_Mapping = subTaskChecklist.objects.all().get(id=self.id).taskId.taskTBMapping
        return related_Mapping
    @property
    def Sub_Task_Description(self):
        related_Description = subTaskChecklist.objects.all().get(id=self.id).taskId.taskDescription
        return related_Description
    @property
    def Sub_Task_Occurence(self):
        related_Occurence = subTaskChecklist.objects.all().get(id=self.id).taskId.taskOccurence
        return related_Occurence
    @property
    def Sub_Task_OwnerId(self):
        related_Owner = subTaskChecklist.objects.all().get(id=self.id).taskId.taskOwnerId
        return related_Owner
    @property
    def Sub_Task_IsJE(self):
        related_IsJE = subTaskChecklist.objects.all().get(id=self.id).taskId.isJE
        return related_IsJE
    @property
    def Related_Task_PK(self):
        related_Pk = subTaskChecklist.objects.all().get(id=self.id).taskId.pk
        return related_Pk 
    @property
    def Not_Equal_CT(self): #method to determine if any non-completed subtasks remain
        try:
            related_SubTask_Model = subTaskChecklist.objects.all().filter(taskId=self.taskId).values('subTaskStatus').exclude(subTaskStatus__startswith="CT").count()
            return related_SubTask_Model
        except:
            related_SubTask_Model = subTaskChecklist.objects.all().filter(taskId=self.taskId).values('subTaskStatus').exists()
            if related_SubTask_Model == True:
                return 0
            else:
                return related_SubTask_Model 
    @property
    def Get_Related_Period(self):
        get_Related_Object = subTaskChecklist.objects.all()
        return str(get_Related_Object.get(id=self.id).taskId.entity) + "-" + str(get_Related_Object.get(id=self.id).taskId.taskId) + "-" + str(get_Related_Object.get(id=self.id).taskId.taskYear) + "-" + str(get_Related_Object.get(id=self.id).taskId.taskPeriod)
        #note within template lookup only include as visual subtask if taskPeriod and year also matches
    
    def File_Path(instance, filename):
        return os.path.join("Sub_Tasks", str(instance.taskId), str(instance.subTaskNumber), filename)
    docfile = models.FileField(upload_to=File_Path, default=False) #Note: To consider a way to set the default value equal to a dynamic file template which a user can download, and upload once completed

    def __str__(self):
        return self.subTaskDescription
