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


#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

# class TaskChecklistList(ListView): #Not in use for now
#     model = TaskChecklist

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
