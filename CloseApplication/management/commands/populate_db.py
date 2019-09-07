from django.core.management.base import BaseCommand
from django.utils import timezone

from django.core.management.base import BaseCommand
from django.apps import apps
import csv


class Command(BaseCommand):
    help = 'Creating model objects according the file path specified'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")
        parser.add_argument('--model_name', type=str, help="model name")
        parser.add_argument('--app_ name', type=str, help="django app name that the model is connected to")

    def handle(self, *args, **options):
        file_path = options['path']
        _model = apps.get_model(options['app_name'], options['model_name'])
        with open(file_path, 'rt', encoding="utf8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='|')
            header = next(reader)
            for row in reader:
                print(row['accountNumber'])