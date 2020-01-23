from django.db import models
from django.contrib.auth.models import User
from CompanyMaintain.choices import periodChoices
import datetime


class userDefinedEntity(models.Model):
    entity = models.CharField(max_length=200, default="Select Entity")
    
    def __str__(self):
        return self.entity

#If closeStatus period is closed then all modification of data should be locked during that period
#this feature/functionality is not implemented yet
class closeStatus(models.Model):
    period = models.DateField(("Due Date"), default=datetime.date.today)
    closeStatus = models.CharField(max_length=200, choices=periodChoices, default=periodChoices[0][0])
    entity = models.ForeignKey(userDefinedEntity, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return str(self.period) + "-" + str(self.entity) + "-" + str(self.closeStatus)



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
