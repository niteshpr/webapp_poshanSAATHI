# Generated by Django 3.0.7 on 2020-08-01 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20200801_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='history_count',
            field=models.IntegerField(default=0),
        ),
    ]