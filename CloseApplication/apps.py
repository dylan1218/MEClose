from django.apps import AppConfig

#updated
class MonthEndCloseConfig(AppConfig):
    name = 'CloseApplication'

    def ready(self):
        import CloseApplication.signals
