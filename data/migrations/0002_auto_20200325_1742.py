# Generated by Django 3.0.4 on 2020-03-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='pic',
            field=models.FileField(max_length=120, upload_to=None),
        ),
    ]
