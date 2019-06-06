from django.contrib import admin
from .models import TaskChecklist 
from .models import AccountReconciliationList
from .models import journalEntryApprovalList
from .models import userReviewerMapping
from .models import userDefinedTeam
#.models format of blank.name means current module import, so we are importing Question from models.py
#not updated, needs updating after database schema created
# Register your models here.

admin.site.register(journalEntryApprovalList)
admin.site.register(TaskChecklist)
admin.site.register(AccountReconciliationList)
admin.site.register(userReviewerMapping)
admin.site.register(userDefinedTeam)

