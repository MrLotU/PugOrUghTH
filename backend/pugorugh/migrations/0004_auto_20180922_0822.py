# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-09-22 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0003_dog_age_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdog',
            name='status',
            field=models.CharField(default='u', max_length=255),
        ),
    ]