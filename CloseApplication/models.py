import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#Note to self -- this is where you'll define the database schema
#For example, for a task checklist I would create var fields defined like
#"TaskID", "Task Description", "Task Due Data" "Task Owner" etc
#each class represents a database table, for each checklist should likely have a table
occurenceChoices = (
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly'),
    ('Q', 'Quarterly'),
    ('A', 'Annually'), 
)

statusChoices = (
    ('NS', 'Not Started'),
    ('WT', 'Waiting on Preceding Task'),
    ('IP', 'In-Progress'),
    ('CT', 'Completed'), 
)

approvalChoices = (
    ('Not Started', 'Not Started'),
    ('Waiting on Support', 'Waiting on Support Upload'),
    ('Rejected', 'In-Progress'),
    ('Reverted', 'In-Progress'),
    ('Approved', 'Completed'), 
)

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

# Create your models here.

class TaskChecklist(models.Model):
    taskId = models.CharField(max_length=6)
    taskDescription = models.CharField(max_length=200)
    taskYear = models.IntegerField(max_length=4)
    taskPeriod = models.IntegerField(max_length=2, choices = periodChoices)
    taskOccurence = models.CharField(max_length=2, choices = occurenceChoices)
    taskOwnerId = models.ForeignKey(User, on_delete=models.CASCADE) #to evaluate if this actually works
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
    reconciliationYear = models.IntegerField(max_length=4)
    reconciliationPeriod = models.IntegerField(max_length=2, choices = periodChoices)
    reconciliationOwnerId = models.ForeignKey(User, on_delete=models.CASCADE) #to evaluate if this actually works
    reconciliationStatus = models.CharField(max_length=2, choices = statusChoices)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateField(("Due Date"), default=datetime.date.today)
    entity = models.CharField(max_length=200, default="Select Entity") #this should be a user defined choice field

    def __str__(self):
        return self.accountDescription



class journalEntryApprovalList(models.Model):
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