# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-27 16:39
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0047_goodsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videocover',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='./video/cover/%Y/%m/%d', verbose_name='\u5c01\u9762'),
        ),
    ]
