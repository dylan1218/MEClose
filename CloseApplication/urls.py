from django.urls import path

from . import views

#one to one relationship between urls and views module.
#note second agument to path takes the views.Method/Function from views

urlpatterns = [
    path('', views.index, name='index'),
    path('CloseSummary/', views.summaryView, name='summaryView'),
    path('Task_Checklist/', views.taskList, name='taskList'),
    path('accountRecList/', views.accountRecList, name='accountRecList'),
    path('EntryApprovalList/', views.entryApprovalList, name='EntryApprovalList'),
]

#path takes arguments (Name path for URL, function from views that handles the html file, and description)