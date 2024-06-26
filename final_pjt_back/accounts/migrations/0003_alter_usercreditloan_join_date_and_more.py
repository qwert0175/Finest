# Generated by Django 4.2.13 on 2024-05-22 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_credit_loan_remove_user_deposit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreditloan',
            name='join_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='userdeposit',
            name='join_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='usersaving',
            name='join_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
