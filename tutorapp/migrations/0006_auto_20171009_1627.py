# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-09 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0005_auto_20170828_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userpk',
            field=models.IntegerField(default=-1),
        ),
    ]
