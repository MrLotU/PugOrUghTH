# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-09-22 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0002_auto_20180922_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='age_classification',
            field=models.CharField(default='u', max_length=255),
        ),
    ]