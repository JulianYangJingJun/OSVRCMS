# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-24 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0011_auto_20171024_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videotime',
            field=models.IntegerField(help_text='\u5355\u4f4d\uff1a\u5206\u949f', null=True, verbose_name='\u89c6\u9891\u65f6\u95f4'),
        ),
    ]
