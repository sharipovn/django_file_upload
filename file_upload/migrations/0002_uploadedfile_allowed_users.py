# Generated by Django 5.0.4 on 2024-04-04 05:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='allowed_users',
            field=models.ManyToManyField(blank=True, related_name='allowed_files', to=settings.AUTH_USER_MODEL),
        ),
    ]
