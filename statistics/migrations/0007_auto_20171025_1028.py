# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-25 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0006_appheart_onfirst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appheart',
            name='ONFIRST',
            field=models.IntegerField(default=0, null=True, verbose_name='\u9996\u6b21'),
        ),
    ]
