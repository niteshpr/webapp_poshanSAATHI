# Generated by Django 3.0.7 on 2020-08-01 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20200801_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosage',
            name='height_cm',
        ),
        migrations.RemoveField(
            model_name='dosage',
            name='weight',
        ),
    ]
