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
    #subtasks paths
    path('subtasks/', views.SubTaskChecklist_List.as_view(), name='subtasklist'),
    path('subtasks/<int:pk>', views.SubTaskChecklistDetail.as_view(), name='subtaskdetail'),
    path('subtasks/create', views.SubTaskChecklistCreate.as_view(), name='subcontact_create'),
    path('subtasks/update/<int:pk>', views.SubTaskChecklistUpdate.as_view(), name='subtask_update'),
    path('subtasks/delete/<int:pk>', views.SubTaskChecklistDelete.as_view(), name='subtask_delete'),
    #accountrecs paths
    path('accountrecs/', views.AccountRecList_List.as_view(), name='accountRecList'),
    path('accountrecs/<int:pk>', views.AccountRecListDetail.as_view(), name='accountrecs_detail'),
    path('accountrecs/create', views.AccountRecListCreate.as_view(), name='accountrecs_create'),
    path('accountrecs/update/<int:pk>', views.AccountRecListUpdate.as_view(), name='accountsrecs_update'),
    path('accountrecs/delete/<int:pk>', views.AccountRecListDelete.as_view(), name='accountsrecs_delete'),
    #entryapprovals paths
    path('entryapprovals/', views.EntryApproval_List.as_view(), name='entryapprovallist'),
    path('entryapprovals/<int:pk>', views.EntryApprovalDetail.as_view(), name='entryapprovallist_detail'),
    path('entryapprovals/create', views.EntryApprovalCreate.as_view(), name='entryapprovallist_create'),
    path('entryapprovals/update/<int:pk>', views.EntryApprovalUpdate.as_view(), name='entryapprovallist_update'),
    path('entryapprovals/delete/<int:pk>', views.EntryApprovalDelete.as_view(), name='entryapprovallist_delete'),
    #entitylist paths
    path('entities/', views.Entity_List.as_view(), name='entity_list'),
    path('entities/<int:pk>', views.EntityDetail.as_view(), name='entity_detail'),
    path('entities/create', views.EntityCreate.as_view(), name='entity_create'),
    path('entities/update/<int:pk>', views.EntityUpdate.as_view(), name='entity_update'),
    path('entities/delete/<int:pk>', views.EntityDelete.as_view(), name='entity_delete'),
    #userlist paths
    path('users/', views.UserList_List.as_view(), name='userlist'),
    path('users/<int:pk>', views.UserListDetail.as_view(), name='userlist_detail'),
    path('users/create', views.UserListCreate.as_view(), name='userlist_create'),
    path('users/update/<int:pk>', views.UserListUpdate.as_view(), name='userlist_update'),
    path('users/delete/<int:pk>', views.UserListDelete.as_view(), name='userlist_delete'),
    #teamlist paths
    path('teams/', views.TeamList_List.as_view(), name='teamlist'),
    path('teams/<int:pk>', views.TeamListDetail.as_view(), name='teamlist_detail'),
    path('teams/create', views.TeamListCreate.as_view(), name='teamlist_create'),
    path('teams/update/<int:pk>', views.TeamListUpdate.as_view(), name='teamlist_update'),
    path('teams/delete/<int:pk>', views.TeamListDelete.as_view(), name='teamlist_delete'),
]

#path takes arguments (Name path for URL, function from views that handles the html file, and description)