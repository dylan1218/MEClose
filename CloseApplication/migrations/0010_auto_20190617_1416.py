# Generated by Django 2.2.2 on 2019-06-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloseApplication', '0009_remove_taskchecklist_taskstatus'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='taskchecklist',
            name='unique_EntityUser',
        ),
        migrations.AddConstraint(
            model_name='taskchecklist',
            constraint=models.UniqueConstraint(fields=('taskId', 'entity', 'taskPeriod', 'taskYear'), name='unique_EntityUser'),
        ),
    ]
