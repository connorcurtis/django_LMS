# Generated by Django 2.2 on 2022-01-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='is_graded',
            field=models.BooleanField(default=False),
        ),
    ]
