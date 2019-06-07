import datetime
from django.db import models
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

#Idea - Add a field to mapp all tasks, reconciliations and JE's to a FSLI
class userDefinedTeam(models.Model):
    team = models.CharField(max_length=200)
    teamOwner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_teamOwner")
        
    def __str__(self):
        return self.team

# Create your models here. For freignkeys below to consider adding limit_choices_to={'is_staff': True} to prevent admins being utilized as values for these fields
class userReviewerMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_user")
    userTeam = models.ForeignKey(userDefinedTeam, on_delete=models.PROTECT, related_name="user_team") #consider setting delete to cascade or default, and giving a default value
    userManager = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_Manager") 
    userReviewer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_Reviewer") #the assigned reviewer can be different than the direct manager (i.e. Accountant -> Senior Accountant -> Manager, where senior reviews)
    systemIdentifier = models.CharField(max_length=200)

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
    subTaskNumber = models.IntegerField(max_length=2, default=1) #For breaking out tasks into parts and having difference preparers. Note might have to create the subtask field under a separate database model
    taskDescription = models.CharField(max_length=200)
    taskYear = models.IntegerField(max_length=4) #note - should remove taskYear and taskPeriod and create a method attribute based off of due date instead
    taskPeriod = models.IntegerField(max_length=2, choices = periodChoices)
    taskOccurence = models.CharField(max_length=2, choices = occurenceChoices)
    taskOwnerId = models.ForeignKey(User, on_delete=models.PROTECT) #For documentation purposes we want to preserve who the owner of a task was, and as such protect is utilized to not allow deletion of the referenced object
    taskStatus = models.CharField(max_length=2, choices = statusChoices)
    isJE = models.CharField(max_length=3, choices=binaryChoice)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateField(("Due Date"), default=datetime.date.today)
    entity = models.CharField(max_length=200, default="Select Entity") #this should be a user defined choice field
    
    def __str__(self):
        return self.taskDescription

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
    entity = models.CharField(max_length=200, default="Select Entity") #this should be a user defined choice field

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

    entity = models.CharField(max_length=200, default="Select Entity") #this should be a user defined choice field
    entryNumber = models.CharField(max_length=200)
    entryReference = models.CharField(max_length=200)
    entryDescription = models.CharField(max_length=200)
    postingDate = models.DateTimeField('date posted to GL')
    entryReversed = models.BooleanField(default=False)
    reversalNumber = models.CharField(max_length=200, default=None)
    postingUsername = models.CharField(max_length=200)
    postingReviewer = models.CharField(max_length=200) #user defined user-reviewer mapping fields should determine
    supportStatus = models.BooleanField(default=False)
    approvalStatus = models.BooleanField(default=False)
    approvalStatus_Description = models.CharField(max_length=200, choices = approvalChoices)
    approverComments = models.CharField(max_length=200)

    def __str__(self):
        return self.entryDescription