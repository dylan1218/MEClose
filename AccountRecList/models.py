from django.db import models
from django.contrib.auth.models import User
import os
import datetime
from datetime import timedelta
from dateutil import relativedelta

#MEClose imports
from CompanyMaintain.models import userDefinedEntity
from CompanyMaintain.choices import periodChoices, statusChoices
from CompanyMaintain.services import getReviewer

class AccountReconciliationListThresholds(models.Model):
    #to reasses whether these fields havethe appropriate types. 
    dollarValueThreshold = models.CharField(max_length=200, default=0)
    percentValueThreshold = models.CharField(max_length=200, default=0)
    excludedAccounts = models.CharField(max_length=200, default=0)
    def __str__(self): 
        return str(self.id)
        
class AccountReconciliationList(models.Model):

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
    approverComments = models.CharField(max_length=200, blank=True)
    #to get rid of due_date field and add calculated method
    #change pub_date to file upload date/attachment date
    #To add a comment field as optional for the client depending on variance
    # To add an approved field
    # To discuss how to dumcnet approvals 
    
    def File_Path(instance, filename):
        return os.path.join("Account Reconciliations", str(instance.entity), str(instance.accountClosePeriod), str(instance.accountNumber), filename)
    
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
    def reviewer(self):
        reviewerUser = getReviewer(self.reconciliationOwnerId, self.entity)
        return reviewerUser.get_reviewer
    
    @property
    def reconciliationRequired(self):
        percentChangeThreshold = int(AccountReconciliationListThresholds.objects.all().first().dollarValueThreshold)
        dollarChangeThreshold = float(AccountReconciliationListThresholds.objects.all().first().percentValueThreshold)
        excludedAccounts = AccountReconciliationListThresholds.objects.all().first().excludedAccounts
        #converts the 0 string to an interger if the string is equal to 0. 0 indicates the user does not want a filter for specific accounts.
        if excludedAccounts == "0":
            excludedAccounts = int(excludedAccounts)

        #first condition is if client does not want any thresholds
        if percentChangeThreshold == 0 and dollarChangeThreshold == 0 and excludedAccounts == 0:
            return True
        #second condition is if client wants percent and dollar threshold, but not an account filter
        elif percentChangeThreshold != 0 and dollarChangeThreshold != 0 and excludedAccounts == 0:
            if self.accountBalance == 0 and self.accountBalancePriorMonth == 0:
                return False
            elif (self.balanceVarianceMoM / self.accountBalancePriorMonth) > percentChangeThreshold or abs(self.balanceVarianceMoM) > dollarChangeThreshold:
                return True
            else:
                return False
        #third condition is if client wants percent threshold, but no others
        elif percentChangeThreshold !=0 and dollarChangeThreshold == 0 and excludedAccounts == 0:
            if self.accountBalance == 0 and self.accountBalancePriorMonth == 0:
                return False
            elif (self.balanceVarianceMoM / self.accountBalancePriorMonth) > percentChangeThreshold:
                return True
            else:
                return False
        #fourth condition is if clients dollar shreshold, but no others
        elif percentChangeThreshold == 0 and dollarChangeThreshold != 0 and excludedAccounts == 0:
            if self.accountBalance == 0 and self.accountBalancePriorMonth == 0:
                return False
            elif (self.balanceVarianceMoM / self.accountBalancePriorMonth) > percentChangeThreshold:
                return True
            else:
                return False
     

    #To add a required reconciliation calculated method
