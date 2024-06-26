# Generated by Django 4.2.13 on 2024-05-21 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='credit_loan',
        ),
        migrations.RemoveField(
            model_name='user',
            name='deposit',
        ),
        migrations.RemoveField(
            model_name='user',
            name='saving',
        ),
        migrations.CreateModel(
            name='UserSaving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField()),
                ('saving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.saving')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField()),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.deposit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCreditLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField()),
                ('creditloan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.creditloan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='creditloans',
            field=models.ManyToManyField(through='accounts.UserCreditLoan', to='products.creditloan'),
        ),
        migrations.AddField(
            model_name='user',
            name='deposits',
            field=models.ManyToManyField(through='accounts.UserDeposit', to='products.deposit'),
        ),
        migrations.AddField(
            model_name='user',
            name='savings',
            field=models.ManyToManyField(through='accounts.UserSaving', to='products.saving'),
        ),
    ]
