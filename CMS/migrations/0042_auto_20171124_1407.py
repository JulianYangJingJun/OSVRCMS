# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-24 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0041_auto_20171124_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='created_at',
            field=models.DateTimeField(verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
