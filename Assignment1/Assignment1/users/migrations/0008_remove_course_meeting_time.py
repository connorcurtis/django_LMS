# Generated by Django 2.2 on 2022-02-06 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220206_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='meeting_time',
        ),
    ]