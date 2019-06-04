from django.urls import path

from . import views

#one to one relationship between urls and views module.
#note second agument to path takes the views.Method/Function from views

urlpatterns = [
    path('', views.index, name='index'),
    path('task', views.taskList, name='taskList'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]