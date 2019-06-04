from django.contrib import admin
from .models import Question #.models format of blank.name means current module import, so we are importing Question from models.py

# Register your models here.

admin.site.register(Question)
