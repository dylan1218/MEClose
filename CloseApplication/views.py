from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import AccountReconciliationList
from .models import TaskChecklist
from .models import journalEntryApprovalList
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import subTaskChecklist


#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

# class TaskChecklistList(ListView): #Not in use for now
#     model = TaskChecklist

class EntryApproval_List(ListView): #Not in use for now
    template_name = 'CloseApplication/entryapprovallist/entryapprovallist_list.html'
    model = journalEntryApprovalList

class AccountRecList_List(ListView): #Not in use for now
    template_name = 'CloseApplication/accountreclist/accountreclist_list.html'
    model = AccountReconciliationList

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

def accountRecList(request):
    accountRecList_Fields = AccountReconciliationList._meta.get_fields(include_hidden=False)
    accountRecList_Values = AccountReconciliationList.objects.all()
    #template = loader.get_template('polls/index.html')
    context = { #context represents the variables passed to the provided template
        'accountRecList_Fields': accountRecList_Fields,
        'accountRecList_Values': accountRecList_Values,
    }
    #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
    return render(request, 'CloseApplication/accountRecList.html', context)
    #Render takes argument render(request, Name of html template path, context varialbes)



def summaryView(request):
    #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
    return render(request, 'CloseApplication/CloseSummary.html')


