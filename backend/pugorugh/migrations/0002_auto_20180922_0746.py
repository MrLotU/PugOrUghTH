# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-09-22 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpref',
            name='age',
            field=models.CharField(default='b,y,a,s', max_length=255),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='gender',
            field=models.CharField(default='f,m', max_length=255),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='size',
            field=models.CharField(default='s,m,l,xl', max_length=255),
        ),
    ]
