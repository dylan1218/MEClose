from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from CloseApplication.forms import DocumentForm
from .models import TaskChecklist
from .models import subTaskChecklist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [login_required]


@method_decorator(decorators, name='dispatch')
class SubTaskChecklist_List(ListView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_list.html'
    model = subTaskChecklist

@method_decorator(decorators, name='dispatch')
class SubTaskChecklistDetail(DetailView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_detail.html'
    model = subTaskChecklist

@method_decorator(decorators, name='dispatch')
class SubTaskChecklistCreate(CreateView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_form.html'
    model = subTaskChecklist
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class SubTaskChecklistUpdate(UpdateView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_form.html'
    model = subTaskChecklist
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class SubTaskChecklistDelete(DeleteView): 
    template_name = 'CloseApplication/subtaskchecklist/subtaskchecklist_delete.html'
    model = subTaskChecklist

#Start of TaskChecklistDetail views:
@method_decorator(decorators, name='dispatch')
class TaskChecklistDetail(DetailView):
    template_name = 'CloseApplication/taskchecklist/taskchecklist_detail.html'
    model = TaskChecklist

@method_decorator(decorators, name='dispatch')
class TaskChecklistCreate(CreateView):
    template_name = 'CloseApplication/taskchecklist/taskchecklist_form.html'
    model = TaskChecklist
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class TaskChecklistUpdate(UpdateView):
    template_name = 'CloseApplication/taskchecklist/taskchecklist_form.html'
    model = TaskChecklist
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class TaskChecklistDelete(DeleteView):
    template_name = 'CloseApplication/taskchecklist/taskchecklist_delete.html'
    model = TaskChecklist

@method_decorator(decorators, name='dispatch')
class taskList(View):
    template = 'CloseApplication/taskchecklist/taskchecklist_list.html'
    def get(self, request, *args, **kwargs):
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
        return render(request, self.template, context)
        #Render takes argument render(request, Name of html template path, context varialbes)

