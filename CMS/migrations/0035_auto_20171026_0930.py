# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-26 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0034_auto_20171025_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='score',
            field=models.FloatField(null=True, verbose_name='\u8bc4\u5206'),
        ),
        migrations.AlterField(
            model_name='game',
            name='score',
            field=models.FloatField(null=True, verbose_name='\u8bc4\u5206'),
        ),
        migrations.AlterField(
            model_name='video',
            name='score',
            field=models.FloatField(null=True, verbose_name='\u8bc4\u5206'),
        ),
    ]
