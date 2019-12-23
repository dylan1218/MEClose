from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import AccountReconciliationList
from datetime import datetime
from notifications.signals import notify
from .services import Get_Reconciled_Balance
from MonthEndCloseDjango.settings import MEDIA_ROOT
import os

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

@receiver(post_save, sender=AccountReconciliationList)
def get_ReconciledBalance(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        docfile_New = instance.docfile
        docfile_New_Name = os.path.basename(docfile_New.name)
        filePathNew = MEDIA_ROOT + "\\" + instance.File_Path(filename=docfile_New_Name)
        reconciledBalanceGet = Get_Reconciled_Balance(instance.accountClosePeriod.month, instance.accountClosePeriod.year, instance.entity, instance.accountNumber, filePathNew)
        AccountReconciliationList.objects.filter(id=instance.id).update(accountBalanceReconciled=reconciledBalanceGet)
        '''
        currentAccountRec.approverComments = reconciledBalanceGet
        currentAccountRec.save()
        '''
@receiver(pre_save, sender=AccountReconciliationList)
def notifications_AccountReconciliationList(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        reconciliationOwnerId_Previous = obj.reconciliationOwnerId 
        reconciliationOwnerId_New = instance.reconciliationOwnerId
        accountBalanceReconciled_Previous = obj.accountBalanceReconciled
        accountBalanceReconciled_New = instance.accountBalanceReconciled

        if not reconciliationOwnerId_Previous == reconciliationOwnerId_New:
            notify.send(instance.reconciliationOwnerId, recipient=instance.reconciliationOwnerId, verb='Account reconciliation XYZ has been assigned to you for MM-YYYY')

        if not accountBalanceReconciled_Previous == accountBalanceReconciled_New:
            print("Change in reconciled status")#Temporary result, to change at a later point