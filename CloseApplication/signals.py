from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from models import TaskChecklist, subTaskChecklist