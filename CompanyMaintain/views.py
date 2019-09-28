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
from .models import userDefinedEntity
from .models import userReviewerMapping
from .models import userDefinedTeam
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [login_required]


#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

# class TaskChecklistList(ListView): #Not in use for now
#     model = TaskChecklist

#Start of userDefinedTeam views:
@method_decorator(decorators, name='dispatch')
class TeamList_List(ListView): 
    template_name = 'CloseApplication/teamlist/teamlist_list.html'
    model = userDefinedTeam

@method_decorator(decorators, name='dispatch')
class TeamListDetail(DetailView): 
    template_name = 'CloseApplication/teamlist/teamlist_detail.html'
    model = userDefinedTeam

@method_decorator(decorators, name='dispatch')
class TeamListCreate(CreateView): 
    template_name = 'CloseApplication/teamlist/teamlist_form.html'
    model = userDefinedTeam
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class TeamListUpdate(UpdateView): 
    template_name = 'CloseApplication/teamlist/teamlist_form.html'
    model = userDefinedTeam
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class TeamListDelete(DeleteView): 
    template_name = 'CloseApplication/teamlist/teamlist_delete.html'
    model = userDefinedTeam

#Start of userReviewerMapping views:
@method_decorator(decorators, name='dispatch')
class UserList_List(ListView): 
    template_name = 'CloseApplication/userlist/userlist_list.html'
    model = userReviewerMapping

@method_decorator(decorators, name='dispatch')
class UserListDetail(DetailView): 
    template_name = 'CloseApplication/userlist/userlist_detail.html'
    model = userReviewerMapping

@method_decorator(decorators, name='dispatch')
class UserListCreate(CreateView): 
    template_name = 'CloseApplication/userlist/userlist_form.html'
    model = userReviewerMapping
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class UserListUpdate(UpdateView): 
    template_name = 'CloseApplication/userlist/userlist_form.html'
    model = userReviewerMapping
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class UserListDelete(DeleteView): 
    template_name = 'CloseApplication/userlist/userlist_delete.html'
    model = userReviewerMapping


#Start of userDefinedEntity views:
@method_decorator(decorators, name='dispatch')
class Entity_List(ListView): 
    template_name = 'CloseApplication/entitylist/entitylist_list.html'
    model = userDefinedEntity

@method_decorator(decorators, name='dispatch')
class EntityDetail(DetailView): 
    template_name = 'CloseApplication/entitylist/entitylist_detail.html'
    model = userDefinedEntity

@method_decorator(decorators, name='dispatch')
class EntityCreate(CreateView): 
    template_name = 'CloseApplication/entitylist/entitylist_form.html'
    model = userDefinedEntity
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class EntityUpdate(UpdateView): 
    template_name = 'CloseApplication/entitylist/entitylist_form.html'
    model = userDefinedEntity
    fields = '__all__'

@method_decorator(decorators, name='dispatch')
class EntityDelete(DeleteView): 
    template_name = 'CloseApplication/entitylist/entitylist_delete.html'
    model = userDefinedEntity
