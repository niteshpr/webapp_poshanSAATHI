# Generated by Django 3.0.7 on 2020-08-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20200801_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='bmi1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='bmi2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='bmi3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
