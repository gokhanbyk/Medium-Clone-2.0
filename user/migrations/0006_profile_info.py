# Generated by Django 4.2.4 on 2023-09-15 13:37

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='info',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
