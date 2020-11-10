# Generated by Django 3.1.3 on 2020-11-10 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('body', models.TextField(default='', max_length=250)),
                ('date_published', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
