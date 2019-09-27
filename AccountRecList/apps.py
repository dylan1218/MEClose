from django.apps import AppConfig

#updated
class AccountRecListConfig(AppConfig):
    name = 'AccountRecList'

    def ready(self):
        import AccountRecList.signals
