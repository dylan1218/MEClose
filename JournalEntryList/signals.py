from django.conf import settings
from django.db.models.signals import pre_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import journalEntryApprovalList
from notifications.signals import notify
