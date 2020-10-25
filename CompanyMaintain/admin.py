from django.contrib import admin
from .models import userDefinedEntity, userDefinedTeam, userReviewerMapping

#.models format of blank.name means current module import, so we are importing Question from models.py
#not updated, needs updating after database schema created
# Register your models here.
admin.site.register(userDefinedEntity)
admin.site.register(userDefinedTeam)
admin.site.register(userReviewerMapping)
