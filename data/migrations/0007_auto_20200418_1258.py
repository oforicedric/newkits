# Generated by Django 2.1.5 on 2020-04-18 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20200326_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='club',
            name='pic',
        ),
    ]
