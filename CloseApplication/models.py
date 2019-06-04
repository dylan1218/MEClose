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

    def __str__(self):
        return self.taskDescription

class AccountReconciliationList(models.Model):
    accountNumber = models.CharField(max_length=50)
    accountDescription = models.CharField(max_length=200)
    reconciliationYear = models.IntegerField(max_length=4)
    reconciliationPeriod = models.IntegerField(max_length=2, choices = periodChoices)
    reconciliationOwnerId = models.ForeignKey(User, on_delete=models.CASCADE) #to evaluate if this actually works
    reconciliationStatus = models.CharField(max_length=2, choices = statusChoices)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.accountDescription

class Question(models.Model):
    question_text = models.CharField(max_length=200) #.CharField describes field type of text, max 200
    pub_date = models.DateTimeField('date published') #.DateTimeField describes field as date
    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_yesterday(self):
        return self.pub_date == timezone.now() - datetime.timedelta(days=1)

#note I added was_published_yesterday
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #each choice associated with a question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
#each subclass of django.db.models.Model (i.e. Question/Choice) takes variables
#which represent database field names