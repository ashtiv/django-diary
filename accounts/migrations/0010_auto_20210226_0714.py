# Generated by Django 3.1.7 on 2021-02-26 07:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210226_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='dardate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
