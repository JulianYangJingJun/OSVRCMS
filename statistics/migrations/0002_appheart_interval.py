# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-26 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appheart',
            name='INTERVAL',
            field=models.IntegerField(default=0, null=True, verbose_name='\u5fc3\u8df3\u95f4\u9694'),
        ),
    ]
