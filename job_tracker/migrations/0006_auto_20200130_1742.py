# Generated by Django 2.2.9 on 2020-01-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_tracker', '0005_auto_20200129_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='followup',
            field=models.DateField(blank=True, null=True),
        ),
    ]
