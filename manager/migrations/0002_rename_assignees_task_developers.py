# Generated by Django 4.2.2 on 2023-06-09 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assignees',
            new_name='developers',
        ),
    ]
