from django.conf import settings
from django.db.models.signals import pre_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import AccountReconciliationList
from datetime import datetime
from notifications.signals import notify
from services import Get_Reconciled_Balance

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

@receiver(pre_save, sender=AccountReconciliationList)
def notifications_AccountReconciliationList(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        reconciliationOwnerId_Previous = obj.reconciliationOwnerId 
        reconciliationOwnerId_New = instance.reconciliationOwnerId
        docfile_Previous = obj.docfile
        docfile_New = instance.docfile
        if not reconciliationOwnerId_Previous == reconciliationOwnerId_New:
            notify.send(instance.reconciliationOwnerId, recipient=instance.reconciliationOwnerId, verb='Account reconciliation XYZ has been assigned to you for MM-YYYY')
        if not docfile_Previous == docfile_New:
            print(docfile_New.path)
            Get_Reconciled_Balance(instance.accountClosePeriod.month, instance.accountClosePeriod.year, instance.entity, instance.accountNumber, docfile_New.path)
