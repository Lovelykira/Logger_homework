# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
