# Generated by Django 3.0.6 on 2021-09-17 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(default='NULL'),
        ),
    ]
