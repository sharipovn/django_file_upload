# Generated by Django 5.0.4 on 2024-04-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0003_uploadedfile_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]