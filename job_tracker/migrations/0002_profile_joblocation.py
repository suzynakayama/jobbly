# Generated by Django 2.2.9 on 2020-01-27 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='joblocation',
            field=models.CharField(default='Toronto, ON', max_length=200),
        ),
    ]