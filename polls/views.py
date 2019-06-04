from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Question
from django.template import loader

#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #returns array of ordered questions
    template = loader.get_template('polls/index.html')
    context = { #context represents the variables passed to the provided template
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
    return render(request, 'polls/index.html', context)

def taskList(request):
    return HttpResponse("This is a task list message")
# Create your views here.

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)