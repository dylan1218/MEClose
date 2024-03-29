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
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from notifications.models import Notification
from django.contrib.auth.models import User
from .serializers import UserSerializer, NotificationSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [login_required]

#MEClose
from .serializers import UserSerializer, NotificationSerializer, TaskChecklistSerializer, subTaskChecklistSerializer, userDefinedEntitySerializer, AccountReconciliationListSerializer
from TaskCheckList.models import TaskChecklist, subTaskChecklist
from CompanyMaintain.models import userDefinedEntity
from AccountRecList.models import AccountReconciliationList

#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

# class TaskChecklistList(ListView): #Not in use for now
#     model = TaskChecklist

###########
#API Views#
###########
@method_decorator(decorators, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

@method_decorator(decorators, name='dispatch')
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

@method_decorator(decorators, name='dispatch')
class TaskChecklistViewSet(viewsets.ModelViewSet):
    queryset = TaskChecklist.objects.all()
    serializer_class = TaskChecklistSerializer

@method_decorator(decorators, name='dispatch')
class subTaskChecklistViewSet(viewsets.ModelViewSet):
    queryset = subTaskChecklist.objects.all()
    serializer_class = subTaskChecklistSerializer  

@method_decorator(decorators, name='dispatch')
class userDefinedEntityViewSet(viewsets.ModelViewSet):
    queryset = userDefinedEntity.objects.all()
    serializer_class = userDefinedEntitySerializer  

@method_decorator(decorators, name='dispatch')
class AccountReconciliationListViewSet(viewsets.ModelViewSet):
    queryset = AccountReconciliationList.objects.all()
    serializer_class = AccountReconciliationListSerializer 