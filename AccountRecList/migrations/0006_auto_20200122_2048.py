# Generated by Django 2.2.2 on 2020-01-23 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountRecList', '0005_accountreconciliationlist_accountbalancereconciled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountreconciliationlist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='date published'),
        ),
    ]
