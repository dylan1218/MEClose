# Generated by Django 2.2.2 on 2020-01-23 01:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyMaintain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='closeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.date.today, verbose_name='Due Date')),
                ('closeStatus', models.CharField(choices=[('Opened', 'Opened'), ('Closed', 'Closed'), ('Late Entry', 'Late Entry')], default='Opened', max_length=200)),
                ('entity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='CompanyMaintain.userDefinedEntity')),
            ],
        ),
    ]