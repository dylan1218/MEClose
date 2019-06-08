from django.urls import path

from . import views

#one to one relationship between urls and views module.
#note second agument to path takes the views.Method/Function from views

urlpatterns = [
    #path('', views.index, name='index'),
    path('CloseSummary/', views.summaryView, name='summaryView'),
    path('TaskChecklist', views.TaskChecklistList.as_view(), name='task_checklist'),
    path('tasks/', views.TaskChecklistList.as_view(), name='tasklist'),
    path('tasks/<int:pk>', views.TaskChecklistDetail.as_view(), name='taskdetail'),
    path('tasks/create', views.TaskChecklistCreate.as_view(), name='contact_create'),
    path('tasks/update/<int:pk>', views.TaskChecklistUpdate.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>', views.TaskChecklistDelete.as_view(), name='task_delete'),
    path('accountRecList/', views.accountRecList, name='accountRecList'),
    path('EntryApprovalList/', views.entryApprovalList, name='EntryApprovalList'),
]

#path takes arguments (Name path for URL, function from views that handles the html file, and description)