# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0004_auto_20170627_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppInstall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MACADDRESS', models.CharField(max_length=50, verbose_name='MAC\u5730\u5740')),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('UPDATAD_AT', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ('CREATED_AT',),
            },
        ),
    ]
