# Generated by Django 4.2.13 on 2024-05-21 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositoptions',
            name='intr_rate',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='depositoptions',
            name='intr_rate2',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='savingoptions',
            name='intr_rate',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='savingoptions',
            name='intr_rate2',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]