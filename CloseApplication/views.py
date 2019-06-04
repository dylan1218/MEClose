from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import TaskChecklist
from django.template import loader

#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

def index(request):
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
    return render(request, 'CloseApplication/index.html', context)

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
