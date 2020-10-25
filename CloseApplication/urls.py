from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
import django.contrib.auth.urls

#MonthEndClose imports
from AccountRecList.views import AccountRecList_List, AccountRecListCreate, AccountRecListDelete, AccountRecListDetail, AccountRecListUpdate
from CompanyMaintain.views import Entity_List, EntityCreate, EntityDelete, EntityDetail, EntityUpdate, UserList_List, UserListCreate, UserListDelete, UserListDetail, UserListUpdate, TeamList_List, TeamListCreate, TeamListDelete, TeamListDetail, TeamListUpdate
from JournalEntryList.views import EntryApproval_List, EntryApprovalCreate, EntryApprovalDelete, EntryApprovalDetail, EntryApprovalUpdate
from TaskCheckList.views import TaskChecklist, TaskChecklistCreate, TaskChecklistDelete, TaskChecklistDetail, TaskChecklistUpdate, taskList, subTaskChecklist, SubTaskChecklist_List, SubTaskChecklistCreate, SubTaskChecklistDelete, SubTaskChecklistDetail, SubTaskChecklistUpdate 
from .views import redirect_view, summaryView, notificationView

#one to one relationship between urls and views module.
#note second agument to path takes the views.Method/Function from views

urlpatterns = [
    path('', redirect_view, name='redirect'),
    path('CloseSummary/', summaryView, name='summaryView'),
    path('Notifications/', notificationView, name='notificationView'),
    #tasks paths
    path('tasks/', taskList.as_view(), name='tasklist'),
    path('tasks/detail/<int:pk>', TaskChecklistDetail.as_view(), name='taskdetail'),
    path('tasks/create', TaskChecklistCreate.as_view(), name='contact_create'),
    path('tasks/update/<int:pk>', TaskChecklistUpdate.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>', TaskChecklistDelete.as_view(), name='task_delete'),
    #subtasks paths
    path('subtasks/', SubTaskChecklist_List.as_view(), name='subtasklist'),
    path('subtasks/<int:pk>', SubTaskChecklistDetail.as_view(), name='subtaskdetail'),
    path('subtasks/create', SubTaskChecklistCreate.as_view(), name='subcontact_create'),
    path('subtasks/update/<int:pk>', SubTaskChecklistUpdate.as_view(), name='subtask_update'),
    path('subtasks/delete/<int:pk>', SubTaskChecklistDelete.as_view(), name='subtask_delete'),
    #accountrecs paths
    path('accountrecs/', AccountRecList_List.as_view(), name='accountRecList'),
    path('accountrecs/detail/<int:pk>', AccountRecListDetail.as_view(), name='accountrecs_detail'),
    path('accountrecs/create', AccountRecListCreate.as_view(), name='accountrecs_create'),
    path('accountrecs/update/<int:pk>', AccountRecListUpdate.as_view(), name='accountsrecs_update'),
    path('accountrecs/delete/<int:pk>', AccountRecListDelete.as_view(), name='accountsrecs_delete'),
    #entryapprovals paths
    path('entryapprovals/', EntryApproval_List.as_view(), name='entryapprovallist'),
    path('entryapprovals/detail/<int:pk>', EntryApprovalDetail.as_view(), name='entryapprovallist_detail'),
    path('entryapprovals/create', EntryApprovalCreate.as_view(), name='entryapprovallist_create'),
    path('entryapprovals/update/<int:pk>', EntryApprovalUpdate.as_view(), name='entryapprovallist_update'),
    path('entryapprovals/delete/<int:pk>', EntryApprovalDelete.as_view(), name='entryapprovallist_delete'),
    #entitylist paths
    path('entities/', Entity_List.as_view(), name='entity_list'),
    path('entities/detail/<int:pk>', EntityDetail.as_view(), name='entity_detail'),
    path('entities/create', EntityCreate.as_view(), name='entity_create'),
    path('entities/update/<int:pk>', EntityUpdate.as_view(), name='entity_update'),
    path('entities/delete/<int:pk>', EntityDelete.as_view(), name='entity_delete'),
    #userlist paths
    path('users/', UserList_List.as_view(), name='userlist'),
    path('users/detail/<int:pk>', UserListDetail.as_view(), name='userlist_detail'),
    path('users/create', UserListCreate.as_view(), name='userlist_create'),
    path('users/update/<int:pk>', UserListUpdate.as_view(), name='userlist_update'),
    path('users/delete/<int:pk>', UserListDelete.as_view(), name='userlist_delete'),
    #teamlist paths
    path('teams/', TeamList_List.as_view(), name='teamlist'),
    path('teams/detail/<int:pk>', TeamListDetail.as_view(), name='teamlist_detail'),
    path('teams/create', TeamListCreate.as_view(), name='teamlist_create'),
    path('teams/update/<int:pk>', TeamListUpdate.as_view(), name='teamlist_update'),
    path('teams/delete/<int:pk>', TeamListDelete.as_view(), name='teamlist_delete'),
]

#path takes arguments (Name path for URL, function from views that handles the html file, and description)