# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-20 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0037_auto_20171120_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagesort',
            name='folder_id',
        ),
    ]
