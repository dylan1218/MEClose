from django.apps import AppConfig

#updated
class TaskCheckListConfig(AppConfig):
    name = 'TaskCheckList'

    def ready(self):
        import TaskCheckList.signals
