# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-25 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0021_game_playcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='filepath',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.File', verbose_name='\u8d44\u6e90\u5305'),
        ),
    ]
