# Generated by Django 3.0.5 on 2020-05-18 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='upload_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
