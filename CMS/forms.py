# -*- coding: utf-8 -*-
#!E:\www\python\OSVRCMS\env python
# @Date    : Date
# @Author  : Julian Yang (aqkt_436@163.com)
# @Link    : http://www.abbstyle.com
from django import forms
from CMS.models import *
from captcha.fields import CaptchaField

'''rewriting User form '''
class UserForm(forms.ModelForm):
    password  = forms.CharField(label=(u"用户密码"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        forms.model = User

'''UserProfile表单重写'''
class UserProfileForm(forms.ModelForm):
    class Meta:
        forms.model = UserProfile

'''Device表单重写'''
class DeviceForm(forms.ModelForm):
    pass
    class Meta:
        forms.model = Device

'''Genres表单重写'''
class GenresForm(forms.ModelForm):
    pass
    class Meta:
        forms.model = Genres



'''ImageForm'''
class ImageForm(forms.ModelForm):
    # imageurl = forms.ModelChoiceField(queryset = File.objects.filter(folder_id=3))
    pass
    class Meta:
        forms.model =Image




'''Game表单重写'''
class GameForm(forms.ModelForm):
    # playcount = forms.CharField(label=(u'打开数'), widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    #is_recommend = forms.CharField(label=(u"推荐"), widget=forms.BooleanField(attrs={'class': 'form-control'}))
    #Sort  = forms.ModelMultipleChoiceField(queryset=cms_videosort.objects.all())
    class Meta:
        forms.model = Game

class VideoFrom(forms.ModelForm):
    videourl = forms.CharField(initial='http://',label=(u'视频网址'),widget=forms.URLInput())
    class Meta:
        forms.model = Video

class AdForm(forms.ModelForm):
    class Meta:
        forms.model = Ad

class AppUpdateMessageForm(forms.ModelForm):
    # placeholder = "请输入搜索内容"
    VERSION_CODE        = forms.CharField(label=(u'版本号'),widget=forms.TextInput(attrs={'placeholder': 'format：v0.5-170605-01'}))
    #DOWNLOAD_URL       = forms.CharField(label=(u'下载地址'),widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    #DOWNLOAD_URL_COUNT = forms.IntegerField(label=(u'下载更新次数'),widget=forms.TextInput(attrs={'readonly': 'readonly','value':0}),required=False)
    #VERSION_BIG        = forms.CharField(label=(u'新版本大小(kb)'),widget=forms.TextInput(attrs={'readonly': 'readonly','value':0}),required=False)
    #VERSION_MD5        = forms.CharField(label=(u'文件MD5'),widget=forms.TextInput(attrs={'readonly':'readonly','value':0}),required=False)
    # UPDATE_MESSAGE_CN = forms.CharField(label=(u'升级信息详情(中文)'),widget=forms.TextInput(attrs={'widht':800,'row':100}),)
    class Meta:
        forms.model = AppUpdateMessage

class FirmWareUpdateMessageForm(forms.ModelForm):
    # DOWNLOAD_URL       = forms.CharField(label=(u'下载地址'), widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    # DOWNLOAD_URL_COUNT = forms.IntegerField(label=(u'下载更新次数'),widget=forms.TextInput(attrs={'readonly': 'readonly','value':0}),required=False)
    # VERSION_BIG        = forms.CharField(label=(u'新版本大小(kb)'),widget=forms.TextInput(attrs={'readonly': 'readonly','value':0}),required=False)
    # VERSION_MD5        = forms.CharField(label=(u'文件MD5'),widget=forms.TextInput(attrs={'readonly':'readonly','value':0}),required=False)
    # UPDATE_MESSAGE_CN  = forms.CharField(label=(u'升级信息详情(中文)'),widget=forms.TextInput(attrs={'widht':800,'row':100}),)
    class Meta:
        forms.model = FirmWareUpdateMessage

