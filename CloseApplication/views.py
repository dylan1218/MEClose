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
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [login_required]



#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

# class TaskChecklistList(ListView): #Not in use for now
#     model = TaskChecklist
@login_required()
def redirect_view(request): #redirects to CloseSummary if at index URL
    response = redirect('/ClosePortal/CloseSummary/')
    return response
@login_required()
def summaryView(request):
    return render(request, 'CloseApplication/CloseSummary.html')
@login_required()
def notificationView(request):
    return render(request, 'CloseApplication/NotificationSummary.html')


