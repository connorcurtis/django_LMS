# Generated by Django 2.2 on 2022-02-05 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220205_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]