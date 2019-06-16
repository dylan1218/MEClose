from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .models import AccountReconciliationList
from .models import TaskChecklist
from .models import journalEntryApprovalList
from .models import subTaskChecklist
from .models import userDefinedEntity
from .models import userReviewerMapping
from .models import userDefinedTeam


#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

# class TaskChecklistList(ListView): #Not in use for now
#     model = TaskChecklist

def redirect_view(request): #redirects to CloseSummary if at index URL
    response = redirect('/ClosePortal/CloseSummary/')
    return response

def summaryView(request):
    return render(request, 'CloseApplication/CloseSummary.html')

#Start of subTaskChecklist views:
class SubTaskChecklist_List(ListView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_list.html'
    model = subTaskChecklist

class SubTaskChecklistDetail(DetailView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_detail.html'
    model = subTaskChecklist

class SubTaskChecklistCreate(CreateView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_form.html'
    model = subTaskChecklist
    fields = '__all__'

class SubTaskChecklistUpdate(UpdateView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_form.html'
    model = subTaskChecklist
    fields = '__all__'

class SubTaskChecklistDelete(DeleteView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_delete.html'
    model = subTaskChecklist

#Start of userDefinedTeam views:
class TeamList_List(ListView): 
    template_name = 'CloseApplication/teamlist/teamlist_list.html'
    model = userDefinedTeam

class TeamListDetail(DetailView): 
    template_name = 'CloseApplication/teamlist/teamlist_detail.html'
    model = userDefinedTeam

class TeamListCreate(CreateView): 
    template_name = 'CloseApplication/teamlist/teamlist_form.html'
    model = userDefinedTeam
    fields = '__all__'

class TeamListUpdate(UpdateView): 
    template_name = 'CloseApplication/teamlist/teamlist_form.html'
    model = userDefinedTeam
    fields = '__all__'

class TeamListDelete(DeleteView): 
    template_name = 'CloseApplication/teamlist/teamlist_delete.html'
    model = userDefinedTeam

#Start of userReviewerMapping views:
class UserList_List(ListView): 
    template_name = 'CloseApplication/userlist/userlist_list.html'
    model = userReviewerMapping

class UserListDetail(DetailView): 
    template_name = 'CloseApplication/userlist/userlist_detail.html'
    model = userReviewerMapping

class UserListCreate(CreateView): 
    template_name = 'CloseApplication/userlist/userlist_form.html'
    model = userReviewerMapping
    fields = '__all__'

class UserListUpdate(UpdateView): 
    template_name = 'CloseApplication/userlist/userlist_form.html'
    model = userReviewerMapping
    fields = '__all__'

class UserListDelete(DeleteView): 
    template_name = 'CloseApplication/userlist/userlist_delete.html'
    model = userReviewerMapping


#Start of userDefinedEntity views:
class Entity_List(ListView): 
    template_name = 'CloseApplication/entitylist/entitylist_list.html'
    model = userDefinedEntity

class EntityDetail(DetailView): 
    template_name = 'CloseApplication/entitylist/entitylist_detail.html'
    model = userDefinedEntity

class EntityCreate(CreateView): 
    template_name = 'CloseApplication/entitylist/entitylist_form.html'
    model = userDefinedEntity
    fields = '__all__'

class EntityUpdate(UpdateView): 
    template_name = 'CloseApplication/entitylist/entitylist_form.html'
    model = userDefinedEntity
    fields = '__all__'

class EntityDelete(DeleteView): 
    template_name = 'CloseApplication/entitylist/entitylist_delete.html'
    model = userDefinedEntity

#Start of EntryApproval_List views:
class EntryApproval_List(ListView): 
    template_name = 'CloseApplication/entryapprovallist/entryapprovallist_list.html'
    model = journalEntryApprovalList

class EntryApprovalDetail(DetailView): 
    template_name = 'CloseApplication/entryapprovallist/entryapprovallist_detail.html'
    model = journalEntryApprovalList

class EntryApprovalCreate(CreateView): 
    template_name = 'CloseApplication/entryapprovallist/entryapprovallist_form.html'
    model = journalEntryApprovalList
    fields = '__all__'

class EntryApprovalUpdate(UpdateView): 
    template_name = 'CloseApplication/entryapprovallist/entryapprovallist_form.html'
    model = journalEntryApprovalList
    fields = '__all__'

class EntryApprovalDelete(DeleteView): 
    template_name = 'CloseApplication/entryapprovallist/entryapprovallist_delete.html'
    model = journalEntryApprovalList

#Start of AccountRecList views:
class AccountRecList_List(ListView): 
    template_name = 'CloseApplication/accountreclist/accountreclist_list.html'
    model = AccountReconciliationList

class AccountRecListDetail(DetailView): 
    template_name = 'CloseApplication/accountreclist/accountreclist_detail.html'
    model = AccountReconciliationList

class AccountRecListCreate(CreateView): #Not in use for now
    template_name = 'CloseApplication/accountreclist/accountreclist_form.html'
    model = AccountReconciliationList
    fields = '__all__'

class AccountRecListUpdate(UpdateView):
    template_name = 'CloseApplication/accountreclist/accountreclist_form.html'
    model = TaskChecklist
    fields = '__all__'

class AccountRecListDelete(DeleteView): #Not in use for now
    template_name = 'CloseApplication/accountreclist/accountreclist_delete.html'
    model = AccountReconciliationList


#Start of TaskChecklistDetail views:
class TaskChecklistDetail(DetailView):
    template_name = 'CloseApplication/taskchecklist/taskchecklist_detail.html'
    model = TaskChecklist

class TaskChecklistCreate(CreateView):
    template_name = 'CloseApplication/taskchecklist/taskchecklist_form.html'
    model = TaskChecklist
    fields = '__all__'

class TaskChecklistUpdate(UpdateView):
    template_name = 'CloseApplication/taskchecklist/taskchecklist_form.html'
    model = TaskChecklist
    fields = '__all__'


class TaskChecklistDelete(DeleteView):
    template_name = 'CloseApplication/taskchecklist/taskchecklist_delete.html'
    model = TaskChecklist

def taskList(request):
    TaskChecklist_Fields = TaskChecklist._meta.get_fields(include_hidden=False)
    TaskChecklist_Values = TaskChecklist.objects.all()
    subTasklist_Fields = subTaskChecklist._meta.get_fields(include_hidden=False)
    subTasklist_Values = subTaskChecklist.objects.all()
    context = { #context represents the variables passed to the provided template
        'TaskChecklist_Fields': TaskChecklist_Fields,
        'TaskChecklist_Values': TaskChecklist_Values,
        'subTasklist_Fields': subTasklist_Fields,
        'subTasklist_Values': subTasklist_Values,
    }
    #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
    return render(request, 'CloseApplication/taskchecklist/taskchecklist_list.html', context)
    #Render takes argument render(request, Name of html template path, context varialbes)

# def index(request):
#     latest_question_list = TaskChecklist.objects.order_by('-pub_date')[:5] #returns array of ordered questions
#     TaskChecklist_Fields = TaskChecklist._meta.get_fields(include_hidden=False)
#     TaskChecklist_Values = TaskChecklist.objects.all()
#     #template = loader.get_template('polls/index.html')
#     context = { #context represents the variables passed to the provided template
#         'latest_question_list': latest_question_list,
#         'TaskChecklist_Fields': TaskChecklist_Fields,
#         'TaskChecklist_Values': TaskChecklist_Values,
#     }
#     #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
#     return render(request, 'CloseApplication/index.html', context)

#def accountRecList(request):
#    accountRecList_Fields = AccountReconciliationList._meta.get_fields(include_hidden=False)
#    accountRecList_Values = AccountReconciliationList.objects.all()
#    #template = loader.get_template('polls/index.html')
#    context = { #context represents the variables passed to the provided template
#        'accountRecList_Fields': accountRecList_Fields,
#        'accountRecList_Values': accountRecList_Values,
#    }
#    #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
#    return render(request, 'CloseApplication/accountRecList.html', context)
#    #Render takes argument render(request, Name of html template path, context varialbes)



