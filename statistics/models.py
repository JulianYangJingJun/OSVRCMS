# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
import datetime
from django.db import models
# Create your models here.

class AppHeart(models.Model):
    APPIP = models.CharField(u'IP',max_length=50,null=True)
    #NAME       = models.ForeignKey("User")
    MACADDRESS = models.CharField(u'MAC地址',max_length=50)
    LOGINTIME  = models.CharField(u'初次心跳时间',max_length=500,null=True)
    HEARTRATE  = models.IntegerField(u'心跳频率',null=True,default=0)
    INTERVAL   = models.IntegerField(u'心跳间隔',null=True,default=30)
    ONLINETIME = models.CharField(u"在线时长(s)", max_length=50,null=True)
    ONFIRST    = models.IntegerField(u'首次',null=True,default=0)
    CREATED_AT = models.DateTimeField(u'创建时间',auto_now_add=True)
    UPDATAD_AT = models.DateTimeField(u'更新时间',auto_now=True)
    def online(self):
        try:
            Interval = int(self.INTERVAL)
            Heartrate = int(self.HEARTRATE)
            return  Interval * Heartrate
        except Exception,e:
            return 0
    online.allow_tags = True
    online.short_description = "当日在线时长(s)"

    def __unicode__(self):
        return u"%s" % self.id

    class Meta:
        ordering = ('CREATED_AT',)
        verbose_name = u'客户端心跳检测'
        verbose_name_plural = u'客户端心跳检测'

class AppInstall(models.Model):
    MACADDRESS = models.CharField(u'MAC地址', max_length=50)
    CREATED_AT = models.DateTimeField(u'创建时间', auto_now_add=True)
    UPDATAD_AT = models.DateTimeField(u'更新时间', auto_now=True)
    class Meta:
        ordering = ('CREATED_AT',)
