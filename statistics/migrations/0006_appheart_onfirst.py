# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0005_appinstall'),
    ]

    operations = [
        migrations.AddField(
            model_name='appheart',
            name='ONFIRST',
            field=models.IntegerField(null=True, verbose_name='\u9996\u6b21'),
        ),
    ]
