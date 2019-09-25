from django.contrib.auth.models import User
from notifications.models import Notification
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ['recipient', 'unread', 'actor_object_id', 'verb', 'description']