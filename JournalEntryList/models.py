from django.db import models
from django.contrib.auth.models import User
import os
import datetime
from pandas.tseries.offsets import BDay
import calendar
import pandas as pd
#MEClose imports
from CompanyMaintain.models import userDefinedEntity
from CompanyMaintain.choices import periodChoices, statusChoices, binaryChoice
from CompanyMaintain.services import getReviewer

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
    
    @property
    def reviewer(self):
        reviewerUser = getReviewer(self.postingUsername, self.entity)
        return reviewerUser.get_reviewer_systemIdentifier