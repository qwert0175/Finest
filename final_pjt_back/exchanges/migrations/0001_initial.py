# Generated by Django 5.0.6 on 2024-05-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('cur_unit', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cur_nm', models.CharField(max_length=20)),
                ('deal_bas_r', models.FloatField(max_length=10)),
            ],
        ),
    ]
