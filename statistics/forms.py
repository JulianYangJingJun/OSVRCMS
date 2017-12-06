#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: Julian
@license: Apache Licence 
@contact: aqkt_436@163.com
@site: http://www.abbstyle.com
@software: PyCharm
@file: forms.py
@time: 6/22/2017 2:07 PMs
"""
from django import forms
from statistics.models import *

class AppHeartForm(forms.ModelForm):
    APPIP      = forms.CharField(label=(u'IP'), widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=True)
    #NAME      = models.ForeignKey("User")
    MACADDRESS = forms.CharField(label=(u'MAC地址'), widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=True)
    LOGINTIME  = forms.CharField(label=(u'初次登录时间'), widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=True)
    HEARTRATE  = forms.IntegerField(label=(u'心跳频率'), widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=True)
    INTERVAL   = forms.IntegerField(label=(u'心跳间隔'), widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=True)
    ONLINETIME = forms.CharField(label=(u'在线时长(s)'), widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=True)
    class Meta:
        forms.model = AppHeart

