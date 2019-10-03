from django.db import models
from django.contrib.auth.models import User
import os
import datetime
from datetime import timedelta
from dateutil import relativedelta

#MEClose imports
from CompanyMaintain.models import userDefinedEntity
from CompanyMaintain.choices import periodChoices, statusChoices

class AccountReconciliationListThresholds(models.Model):
    dollarValueThreshold = models.CharField(max_length=200, default=0)
    percentValueThreshold = models.CharField(max_length=200, default=0)
    def __str__(self):
        return str(self.id)
        
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
    accountBalancePriorMonth = models.IntegerField(max_length=200, default=0)
    accountClosePeriod = models.DateField(("As of balance date"), default=datetime.date.today)
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
        return os.path.join("Journal Entries", str(instance.entity), str(instance.accountClosePeriod), str(instance.accountNumber), filename)
    docfile = models.FileField(upload_to=File_Path, default=False) #Note: To consider a way to set the default value equal to a dynamic file template which a user can download, and upload once completed
    def __str__(self):
        return self.accountDescription
    
    @property
    def priorMonthReconciliation(self):   
        firstDayofMonth = datetime.date(self.accountClosePeriod.year,self.accountClosePeriod.month, self.accountClosePeriod.day).replace(day=1)
        priorMonth = firstDayofMonth - timedelta(days=1)
        priorMonthBalance = AccountReconciliationList.objects.all().filter(entity=self.entity, accountNumber=self.accountNumber, accountClosePeriod__month=priorMonth.month)
        if priorMonthBalance.first() is not None: #.first() method is utilized as there should be no more than one match from the prior month.
            return priorMonthBalance.first().accountBalance
        else: 
            return "No prior month found"

    @property
    def balanceVarianceMoM(self):   
        return self.accountBalance - self.accountBalancePriorMonth


    @property
    def reconciliationRequired(self):
        percentChangeThreshold = int(AccountReconciliationListThresholds.all().first().dollarValueThreshold)
        dollarChangeThreshold = int(AccountReconciliationListThresholds.all().first().percentValueThreshold)
        if self.accountBalance == 0 and self.accountBalancePriorMonth == 0:
            return False
        elif (self.balanceVarianceMoM / self.accountBalancePriorMonth) > percentChangeThreshold or abs(self.balanceVarianceMoM) > dollarChangeThreshold:
            return True
        else:
            return False

    #To add a required reconciliation calculated method
