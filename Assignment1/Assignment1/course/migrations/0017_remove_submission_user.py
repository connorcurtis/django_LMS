# Generated by Django 4.0.2 on 2022-03-23 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_assignment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='user',
        ),
    ]