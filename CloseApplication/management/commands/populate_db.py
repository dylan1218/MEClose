from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.apps import apps
import csv
import datetime

from AccountRecList.models import AccountReconciliationList
from CompanyMaintain.choices import statusChoices
from CompanyMaintain.models import userDefinedEntity


#SO reference https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
#Command use python manage.py populate_db --path "C:\Users\Dylan\Downloads\AccountRecImport.csv" --model_name "AccountReconciliationList" --app_name "AccountRecList"
class Command(BaseCommand):
    help = 'Creating model objects according the file path specified'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")
        parser.add_argument('--model_name', type=str, help="model name")
        parser.add_argument('--app_name', type=str, help="django app name that the model is connected to")

    def handle(self, *args, **options):
        file_path = options['path']
        _model = apps.get_model(options['app_name'], options['model_name'])
        with open(file_path, 'rt', encoding="utf8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='|')
            #header = next(reader)
            for row in reader:
                #_object_dict = {key: value for key, value in zip(header, row)}
                #_model.objects.create(**_object_dict)
                #print(row['accountNumber'])
                #_model.objects.create(accountNumber=row['accountNumber'])
                #print(row['accountDescription'])
                #try:
                #    print(User.objects.filter(user=row['reconciliationOwnerId']))
                #except:
                #    print("error")
                create_AccountRec = AccountReconciliationList(
                                    accountNumber=row['accountNumber'], accountDescription=row['accountDescription'], 
                                    accountBalance=row['accountBalance'], accountBalanceReconciled=0,
                                    accountBalancePriorMonth=0,accountClosePeriod=datetime.datetime.strptime(row['accountClosePeriod'],'%Y-%m-%d'),
                                    reconciliationOwnerId=User.objects.filter(username=row['reconciliationOwnerId'])[0],reconciliationStatus=statusChoices[0][0],
                                    pub_date=datetime.date.today, due_date=datetime.date.today,
                                    entity=userDefinedEntity.objects.filter(entity=row['entity'])[0], approvalStatus=False,
                                    approverComments="")
                #create_AccountRec.save()
