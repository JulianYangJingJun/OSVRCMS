# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-25 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0028_auto_20171025_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videopath',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.File', verbose_name='\u89c6\u9891\u6587\u4ef6'),
        ),
    ]
