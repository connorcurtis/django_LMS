# Generated by Django 2.2 on 2022-01-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_profile',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
