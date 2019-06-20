import datetime
import os
from django.db import models
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.models import User
#Note to self -- this is where you'll define the database schema
#For example, for a task checklist I would create var fields defined like
#"TaskID", "Task Description", "Task Due Data" "Task Owner" etc
#each class represents a database table, for each checklist should likely have a table

statusChoices = (
    ('NS', 'Not Started'),
    ('WT', 'Waiting on Preceding Task'),
    ('IP', 'In-Progress'),
    ('CT', 'Completed'), 
)

#this choice field should go away after creating attributes based off of date field
periodChoices = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
)
binaryChoice = (
    ("Yes", "Yes"),
    ("No", "No"),
)

class userDefinedEntity(models.Model):
    entity = models.CharField(max_length=200, default="Select Entity")
    
    def __str__(self):
        return self.entity

#Idea - Add a field to mapp all tasks, reconciliations and JE's to a FSLI
class userDefinedTeam(models.Model):
    team = models.CharField(max_length=200)
    teamOwner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_teamOwner")
    entity = models.ForeignKey(userDefinedEntity, on_delete=models.PROTECT, related_name="entity_userDefinedTeam", default=1)
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['team', 'entity'], name='unique_EntityTeam')
        ]
    
    def __str__(self):
        return str(self.team) + "-" + str(self.entity)
    

# Create your models here. For freignkeys below to consider adding limit_choices_to={'is_staff': True} to prevent admins being utilized as values for these fields
class userReviewerMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_user")
    userTeam = models.ForeignKey(userDefinedTeam, on_delete=models.PROTECT, related_name="user_team") #consider setting delete to cascade or default, and giving a default value
    userManager = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_Manager") 
    userReviewer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_Reviewer") #the assigned reviewer can be different than the direct manager (i.e. Accountant -> Senior Accountant -> Manager, where senior reviews)
    systemIdentifier = models.CharField(max_length=200)
    entity = models.ForeignKey(userDefinedEntity, on_delete=models.PROTECT, related_name="entity_userReviewerMapping", default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'entity'], name='unique_EntityUser')
        ]
        
    def __str__(self):
        return self.systemIdentifier

class TaskChecklist(models.Model):
    
    occurenceChoices = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Q', 'Quarterly'),
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
    due_date = models.DateField(("Due Date"), default=datetime.date.today)
    entity = models.ForeignKey(userDefinedEntity, on_delete=models.PROTECT, related_name="entity_TaskChecklist", default=1)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['taskId', 'entity', 'taskPeriod', 'taskYear'], name='unique_EntityUser')
        ]
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
    #Note I did not add additional fields as                                     the related parent should contain this data 
    #unique contrain entity, taskId, subTaskNumber, year, period
    #class Meta:
    #    constraints = [
    #        models.UniqueConstraint(fields=['taskId', 'subTaskNumber'], name='unique_Subtask')
    #    ]

    @property
    def Not_Equal_CT(self): #method to determine if any non-completed subtasks remain
        try:
            related_SubTask_Model = subTaskChecklist.objects.all().filter(taskId=self.taskId).values('subTaskStatus').exclude(subTaskStatus__startswith="CT").count()
            #related_Period = subTaskChecklist.objects.all().get(id=self.id).taskId.taskPeriod
            #related_Year = subTaskChecklist.objects.all().get(id=self.id).taskId.taskYear
            #related_Entity = subTaskChecklist.objects.all().get(id=self.id).taskId.entity
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
    
    def __str__(self):
        return self.subTaskDescription

class AccountReconciliationList(models.Model):
    accountNumber = models.CharField(max_length=50)
    accountDescription = models.CharField(max_length=200)
    accountBalance = models.IntegerField(max_length=200, default=0)
    reconciliationYear = models.IntegerField(max_length=4) #reconciliation year and period should be based off of a period end date value -- to create that field
    reconciliationPeriod = models.IntegerField(max_length=2, choices = periodChoices)
    reconciliationOwnerId = models.ForeignKey(User, on_delete=models.CASCADE) #to evaluate if this actually works
    reconciliationStatus = models.CharField(max_length=2, choices = statusChoices)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateField(("Due Date"), default=datetime.date.today)
    entity = models.ForeignKey(userDefinedEntity, on_delete=models.PROTECT, related_name="entity_AccountReconciliationList", default=1)
    
    def File_Path(instance, filename):
        return os.path.join(str(instance.entity), str(instance.reconciliationYear), str(instance.reconciliationPeriod), str(instance.accountNumber), filename)
    docfile = models.FileField(upload_to=File_Path, default=False) #Note: To consider a way to set the default value equal to a dynamic file template which a user can download, and upload once completed
    def __str__(self):
        return self.accountDescription



class journalEntryApprovalList(models.Model):
    approvalChoices = (
        ('Not Started', 'Not Started'),
        ('Waiting on Support', 'Waiting on Support Upload'),
        ('Rejected', 'In-Progress'),
        ('Reverted', 'In-Progress'),
        ('Approved', 'Completed'), 
    )

    entity = models.ForeignKey(userDefinedEntity, on_delete=models.PROTECT, related_name="entity_journalEntryApprovalList", default=1)
    entryNumber = models.CharField(max_length=200)
    entryReference = models.CharField(max_length=200)
    entryDescription = models.CharField(max_length=200)
    postingDate = models.DateTimeField('date posted to GL')
    entryReversed = models.BooleanField(default=False)
    reversalNumber = models.CharField(max_length=200, blank=True)
    postingUsername = models.CharField(max_length=200)
    supportStatus = models.BooleanField(default=False)
    approvalStatus = models.BooleanField(default=False)
    approvalStatus_Description = models.CharField(max_length=200, choices = approvalChoices)
    approverComments = models.CharField(max_length=200, blank=True)
    
    def File_Path(instance, filename):
        return os.path.join("Journal Entries", str(instance.entity), str(instance.postingDate.strftime("%Y")), str(instance.postingDate.strftime("%m")), str(instance.entryNumber), filename)
    docfile = models.FileField(upload_to=File_Path, default=False) #Note: To consider a way to set the default value equal to a dynamic file template which a user can download, and upload once completed

    def __str__(self):
        return self.entryDescription