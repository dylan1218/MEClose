from django.contrib.auth.models import User
from notifications.models import Notification
from rest_framework import serializers
from TaskCheckList.models import TaskChecklist, subTaskChecklist
from CompanyMaintain.models import userDefinedEntity

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ['pk','recipient', 'unread', 'actor_object_id', 'verb', 'description']

class TaskChecklistSerializer(serializers.ModelSerializer):
    taskId_taskId = serializers.StringRelatedField(many=True) #taskId_taskId is the related field name to the task checklist on the subtask checklist
    class Meta:
        model = TaskChecklist
        fields = '__all__'

class subTaskChecklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = subTaskChecklist
        fields = '__all__'

class userDefinedEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userDefinedEntity
        fields = '__all__'