from django.db import models
from django.contrib.auth.models import User
import os
import datetime

#MEClose imports
from CompanyMaintain.models import userDefinedEntity
from CompanyMaintain.choices import periodChoices, statusChoices


class AccountReconciliationList(models.Model):
    approvalChoices = (
        ('Not Started', 'Not Started'),
        ('Waiting on Support', 'Waiting on Support Upload'),
        ('Rejected', 'In-Progress'),
        ('Reverted', 'In-Progress'),
        ('Approved', 'Completed'), 
    )
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
    approvalStatus = models.BooleanField(default=False)
    approvalStatus_Description = models.CharField(max_length=200, choices = approvalChoices, default=approvalChoices[0][0])
    approverComments = models.CharField(max_length=200, blank=True)
    #to get rid of due_date field and add calculated method
    #change pub_date to file upload date/attachment date
    #To add a comment field as optional for the client depending on variance
    # To add an approved field
    # To discuss how to dumcnet approvals 
    def File_Path(instance, filename):
        return os.path.join("Journal Entries", str(instance.entity), str(instance.reconciliationYear), str(instance.reconciliationPeriod), str(instance.accountNumber), filename)
    docfile = models.FileField(upload_to=File_Path, default=False) #Note: To consider a way to set the default value equal to a dynamic file template which a user can download, and upload once completed
    def __str__(self):
        return self.accountDescription
    @property
    def balanceVarianceMoM(self): 
        priorMonthBalance = AccountReconciliationList.objects.all().get(id=self.id).accountBalance #Note: This query needs to change in order to actually return the prior month, currently just returns self 
        return self.accountBalance - priorMonthBalance

    #To add a required reconciliation calculated method
