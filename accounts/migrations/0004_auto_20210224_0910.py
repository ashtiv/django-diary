# Generated by Django 3.1.7 on 2021-02-24 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20210223_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
