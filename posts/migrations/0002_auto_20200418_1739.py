# Generated by Django 3.0.5 on 2020-04-18 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Club'),
        ),
    ]
