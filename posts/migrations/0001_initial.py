# Generated by Django 3.0.5 on 2020-04-18 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='user', max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Club')),
            ],
        ),
    ]
