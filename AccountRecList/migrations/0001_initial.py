# Generated by Django 2.2.2 on 2019-10-02 23:04

import AccountRecList.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CompanyMaintain', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountReconciliationList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumber', models.CharField(max_length=50)),
                ('accountDescription', models.CharField(max_length=200)),
                ('accountBalance', models.IntegerField(default=0, max_length=200)),
                ('accountBalancePriorMonth', models.IntegerField(default=0, max_length=200)),
                ('accountClosePeriod', models.DateField(default=datetime.date.today, verbose_name='As of balance date')),
                ('reconciliationStatus', models.CharField(choices=[('NS', 'Not Started'), ('WT', 'Waiting on Preceding Task'), ('IP', 'In-Progress'), ('CT', 'Completed')], max_length=2)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('due_date', models.DateField(default=datetime.date.today, verbose_name='Due Date')),
                ('approvalStatus', models.BooleanField(default=False)),
                ('approvalStatus_Description', models.CharField(choices=[('Not Started', 'Not Started'), ('Waiting on Support', 'Waiting on Support Upload'), ('Rejected', 'In-Progress'), ('Reverted', 'In-Progress'), ('Approved', 'Completed')], default='Not Started', max_length=200)),
                ('approverComments', models.CharField(blank=True, max_length=200)),
                ('docfile', models.FileField(default=False, upload_to=AccountRecList.models.AccountReconciliationList.File_Path)),
                ('entity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='entity_AccountReconciliationList', to='CompanyMaintain.userDefinedEntity')),
                ('reconciliationOwnerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
