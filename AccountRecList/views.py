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
from .models import AccountReconciliationList



#these functions return a response to a given web page. Each of these functions coorespond
#to a web page name. Note that each method in here has a one to one relationship to url.py

# class TaskChecklistList(ListView): #Not in use for now
#     model = TaskChecklist

class AccountRecList_List(View):
    template = 'CloseApplication/accountreclist/accountreclist_list.html'
    model = AccountReconciliationList
    form_class = DocumentForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        AccountReconciliationList_Values = AccountReconciliationList.objects.all()
        context = { #context represents the variables passed to the provided template
            'AccountReconciliationList_Values': AccountReconciliationList_Values,
            'form': form,
        }
        #return HttpResponse(template.render(context, request)) is the same as return render(request, 'polls/index.html', context)
        return render(request, self.template, context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            data_Record = AccountReconciliationList.objects.get(pk=int(request.POST['list_pk'])) #This is not a great approach but does the job for now -- theoertically user could change the front-end id before submitting.
            data_Record.docfile = request.FILES['docfile']
            data_Record.save()
            return HttpResponseRedirect(reverse('accountRecList'))
        else:
            form=DocumentForm()
            return render(request, self.template, {'form': form})


class AccountRecListDetail(DetailView): 
    template_name = 'CloseApplication/accountreclist/accountreclist_detail.html'
    model = AccountReconciliationList

class AccountRecListCreate(CreateView): #Not in use for now
    template_name = 'CloseApplication/accountreclist/accountreclist_form.html'
    model = AccountReconciliationList
    fields = '__all__'

class AccountRecListUpdate(UpdateView):
    template_name = 'CloseApplication/accountreclist/accountreclist_form.html'
    model = AccountReconciliationList
    fields = '__all__'

class AccountRecListDelete(DeleteView): #Not in use for now
    template_name = 'CloseApplication/accountreclist/accountreclist_delete.html'
    model = AccountReconciliationList