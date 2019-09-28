from django.urls import path, include
from rest_framework import routers
from . import views
from django.contrib.auth import views as auth_views
import django.contrib.auth.urls

#MonthEndClose imports
from .views import  UserViewSet, NotificationViewSet, TaskChecklistViewSet, subTaskChecklistViewSet, userDefinedEntityViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'taskchecklist', TaskChecklistViewSet)
router.register(r'subtaskchecklist', subTaskChecklistViewSet)
router.register(r'userdefinedentity', userDefinedEntityViewSet)


#one to one relationship between urls and views module.
#note second agument to path takes the views.Method/Function from views

urlpatterns = [
    #API paths
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

#path takes arguments (Name path for URL, function from views that handles the html file, and description)