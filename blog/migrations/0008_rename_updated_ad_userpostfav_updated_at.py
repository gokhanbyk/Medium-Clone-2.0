# Generated by Django 4.2.4 on 2023-09-18 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_userpostfav'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpostfav',
            old_name='updated_ad',
            new_name='updated_at',
        ),
    ]