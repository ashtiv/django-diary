# Generated by Django 3.1.7 on 2021-02-26 07:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_todolist_dardate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='dardate',
            field=models.DateField(default=datetime.datetime(2021, 2, 26, 7, 14, 20, 285595, tzinfo=utc)),
        ),
    ]
