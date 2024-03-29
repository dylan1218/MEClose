# Generated by Django 2.2.2 on 2020-01-23 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountRecList', '0006_auto_20200122_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountreconciliationlist',
            name='accountBalance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=17),
        ),
        migrations.AlterField(
            model_name='accountreconciliationlist',
            name='accountBalancePriorMonth',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=17),
        ),
        migrations.AlterField(
            model_name='accountreconciliationlist',
            name='accountBalanceReconciled',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=17),
        ),
    ]
