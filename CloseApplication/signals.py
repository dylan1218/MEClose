from django.conf import settings
from django.db.models.signals import pre_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import TaskChecklist, subTaskChecklist

#signal logic -- if subtask status change, check if all subtasks completed, if so generate
#parent task and associated subtasks (not need to confirm not exists before creation)
@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

@receiver(pre_save, sender=subTaskChecklist)
def do_something_if_changed(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass # Object is new, so field hasn't technically changed, but you may want to do something else here.
    else:
        previous_Value = obj.subTaskStatus
        new_Value = instance.subTaskStatus
        if not previous_Value == new_Value: # Field has changed
            print("Field has changed from " + str(previous_Value) + " to " + str(new_Value))
            if str(new_Value) == "CT" and instance.Not_Equal_CT == 1: #if equal to 1 on pre_save indicates 0 after save, thus all subtasks for associated parent task are completed and a rollover is required. 
                print(instance.Not_Equal_CT) #research how to call on 
                print("subTask completed")

            #note to self, watch out for case where not completed = 0, but no associated subtasks