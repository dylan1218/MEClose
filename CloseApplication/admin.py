from django.contrib import admin
from .models import TaskChecklist #.models format of blank.name means current module import, so we are importing Question from models.py
#not updated, needs updating after database schema created
# Register your models here.

admin.site.register(TaskChecklist)
