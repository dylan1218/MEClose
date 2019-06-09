from django.urls import path

from . import views

#one to one relationship between urls and views module.
#note second agument to path takes the views.Method/Function from views

urlpatterns = [
    path('', views.redirect_view, name='redirect'),
    path('CloseSummary/', views.summaryView, name='summaryView'),
    #tasks paths
    path('tasks/', views.taskList, name='tasklist'),
    path('tasks/<int:pk>', views.TaskChecklistDetail.as_view(), name='taskdetail'),
    path('tasks/create', views.TaskChecklistCreate.as_view(), name='contact_create'),
    path('tasks/update/<int:pk>', views.TaskChecklistUpdate.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>', views.TaskChecklistDelete.as_view(), name='task_delete'),
    #accountrecs paths
    path('accountrecs/', views.AccountRecList_List.as_view(), name='accountRecList'),
    path('accountrecs/<int:pk>', views.AccountRecListDetail.as_view(), name='accountrecs_detail'),
    path('accountrecs/create', views.AccountRecListCreate.as_view(), name='accountrecs_create'),
    path('accountrecs/update/<int:pk>', views.AccountRecListUpdate.as_view(), name='accountsrecs_update'),
    path('accountrecs/delete/<int:pk>', views.AccountRecListDelete.as_view(), name='accountsrecs_delete'),
    #entryapprovals paths
    path('entryapprovals/', views.EntryApproval_List.as_view(), name='EntryApprovalList'),
]

#path takes arguments (Name path for URL, function from views that handles the html file, and description)