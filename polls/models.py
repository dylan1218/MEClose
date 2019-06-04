import datetime
from django.db import models
from django.utils import timezone
#Note to self -- this is where you'll define the database schema
#For example, for a task checklist I would create var fields defined like
#"TaskID", "Task Description", "Task Due Data" "Task Owner" etc
#each class represents a database table, for each checklist should likely have a table

# Create your models here.
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