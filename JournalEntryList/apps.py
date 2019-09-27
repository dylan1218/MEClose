from django.apps import AppConfig

#updated
class JournalEntryListConfig(AppConfig):
    name = 'JournalEntryList'

    def ready(self):
        import JournalEntryList.signals
