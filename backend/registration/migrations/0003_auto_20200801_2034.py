# Generated by Django 3.0.7 on 2020-08-01 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='visit_count',
            new_name='history_count',
        ),
    ]