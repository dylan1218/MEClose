from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import AccountReconciliationList
from .models import TaskChecklist
from .models import journalEntryApprovalList
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

class TaskChecklistList(ListView):
    model = TaskChecklist

class TaskChecklistDetail(DetailView):
    model = TaskChecklist

class TaskChecklistCreate(CreateView):
    model = TaskChecklist
    fields = '__all__'

class TaskChecklistUpdate(UpdateView):
    model = TaskChecklist
    fields = '__all__'

class TaskChecklistDelete(DeleteView):
    model = TaskChecklist

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

def taskList(request):
    latest_question_list = TaskChecklist.objects.order_by('-pub_date')[:5] #returns array of ordered questions
    TaskChecklist_Fields = TaskChecklist._meta.get_fields(include_hidden=False)
    TaskChecklist_Values = TaskChecklist.objects.all()
    #template = loader.get_template('polls/index.html')
    context = { #context represents the variables passed to the provided template
        'latest_question_list': latest_question_list,
        'TaskChecklist_Fields': TaskChecklist_Fields,
        'TaskChecklist_Values': TaskChecklist_Values,
    }
    #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
    return render(request, 'CloseApplication/Task_Checklist.html', context)
    #Render takes argument render(request, Name of html template path, context varialbes)

def entryApprovalList(request):
    journalEntryApprovalList_Fields = journalEntryApprovalList._meta.get_fields(include_hidden=False)
    journalEntryApprovalList_Values = journalEntryApprovalList.objects.all()
    #template = loader.get_template('polls/index.html')
    context = { #context represents the variables passed to the provided template
        'journalEntryApprovalList_Fields': journalEntryApprovalList_Fields,
        'journalEntryApprovalList_Values': journalEntryApprovalList_Values,
    }
    #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
    return render(request, 'CloseApplication/EntryApproval_Checklist.html', context)

def summaryView(request):
    #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
    return render(request, 'CloseApplication/CloseSummary.html')


