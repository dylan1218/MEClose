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
from .models import journalEntryApprovalList
from CloseApplication.forms import DocumentForm



#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

# class TaskChecklistList(ListView): #Not in use for now
#     model = TaskChecklist

#Start of EntryApproval_List views:
class EntryApproval_List(View):
    template = 'CloseApplication/entryapprovallist/entryapprovallist_list.html'
    model = journalEntryApprovalList
    form_class = DocumentForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        journalEntryApprovalList_Values = journalEntryApprovalList.objects.all()
        context = { #context represents the variables passed to the provided template
            'journalEntryApprovalList_Values': journalEntryApprovalList_Values,
            'form': form,
        }
        #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
        return render(request, self.template, context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            data_Record = journalEntryApprovalList.objects.get(pk=int(request.POST['list_pk'])) #This is not a great approach but does the job for now -- theoertically user could change the front-end id before submitting.
            data_Record.docfile = request.FILES['docfile']
            data_Record.save()
            return HttpResponseRedirect(reverse('entryapprovallist'))
        else:
            form=DocumentForm()
            return render(request, self.template, {'form': form})



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

