# -*- coding: utf-8 -*-
#!E:\www\python\OSVRCMS\env python
# @DateTime    : 2017/4/13 10:34
# @Author  : Julian Yang (aqkt_436@163.com)
# @Link    : http://www.abbstyle.com
from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib import admin
from form_utils.widgets import ImageWidget
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from CMS.common.FileStorage import FileStorage
from CMS.common.FileMd5 import FileMd5
from filer.models import *
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User as auth_user
from easy_thumbnails.fields import ThumbnailerImageField
# from django.http import HttpRequest
#import md5_hex
#import os
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
# from CMS.md5_hex import Md5_hex

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())



#
# class GoodsImage(models.Model):
#     Img = ThumbnailerImageField(upload_to='images/',blank=True)
#



'''用户注册信息'''
class User(models.Model):
    name       = models.CharField(u'用户名',max_length=255)
    email      = models.EmailField(u'邮箱')
    password   = models.CharField(u'用户密码',max_length=100)
    avatars    = models.ImageField(u'用户头像',upload_to='./user/avatars/%Y-%m-%d/', null =True, blank=True)
    mobil      = models.CharField(u'手机号码', max_length=13,null=True)
    token      = models.CharField('TOKEN', max_length=100)
    ip         = models.GenericIPAddressField(u'登录IP',null=True)
    created_at = models.DateTimeField(u'创建时间',auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间',auto_now=True)
    class Meta:
        ordering = ('created_at',)
        verbose_name = "注册用户信息" #默认多出S
        verbose_name_plural="注册用户信息" #复数用法
    #图片显示
    def avatarss(self):
        return '<img src="/media/%s"/  width="50"/ height="50"/ >' % self.avatars
    avatarss.allow_tags = True
    avatarss.short_description = "用户头像"
    def __unicode__(self):
        return u"%s" % self.name
'''用户详细信息'''
class UserProfile(models.Model):
    credentialName = models.CharField(u'证件姓名',max_length=70)
    credentialType_choices =(
        (0,u"身份证"),
        (1,u"护照"),
    )
    credentialType = models.IntegerField(u'证件类型',choices=credentialType_choices,default=0)
    credentialNum  = models.IntegerField(u'证件号')
    credentialPhoto     = models.ImageField(u'证件照正面',upload_to='./user/credential/front/%Y/%m/%d',blank=True,null=True)
    credentialPhotoBack = models.ImageField(u'证件照背面',upload_to='./user/credential/back/%Y/%m/%d',blank=True,null=True)
    adop_choices = (
        (0, u'待审核'),
        (1, u'通过'),
        (2, u'未通过'),
    )
    adopt          = models.IntegerField(u'审核',choices=adop_choices,default=0)
    created_at     = models.DateTimeField(u'创建时间',auto_now_add=True)
    updated_at     = models.DateTimeField(u'更新时间',auto_now=True)
    # def __unicode__(self):
    #     return u"%s" % self.credentialName
    class Meta:
        ordering=('created_at',)
        verbose_name = '开发者申请信息'
        verbose_name_plural = '开发者申请信息'
    # 图片显示
    # def image(self):
    #     return '<img src="/media/%s"/>' % self.credentialPhoto
    # image.allow_tags = True
class Index(models.Model):
     from_id = models.IntegerField(u'来自ID')
     name    = models.CharField(u'名称',max_length=255)
     type    = models.IntegerField(u'类型')
     img     = models.CharField(u'主图',max_length=500)
     score   = models.FloatField(u'评分',null=True,blank=True)
     def __unicode__(self):
          return u"%s" % self.name
#
# UserToken
#
class UserToken(models.Model):
    from django.contrib.auth.models import User
    key = models.CharField(u'Token',max_length=255)
    created_at  = models.DateTimeField(u'创建时间')
    user_id     = models.IntegerField(u'用户ID')
    expire_date = models.DateTimeField(u'失效时间',null=True)
    def __unicode__(self):
        return u"%s"% self.key

#----------------------------------------游戏管理----------------------------------------
#游戏类型
class Genres(models.Model):
    name = models.CharField(u'类型名称',max_length=30)
    shortname = models.CharField(u'简称',max_length=10,default=None)
    created_at = models.DateTimeField(u'创建时间',auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间',auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'游戏类型'
        verbose_name_plural = u'游戏类型'
#游戏平台
class Device(models.Model):
    name       = models.CharField(u'设备名称',max_length=30)
    shortname  = models.CharField(u'简称',max_length=5,null=True)
    img        = models.ImageField(u'图标',upload_to='./device/%Y/%m/%d',blank=True,null=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'游戏平台'
        verbose_name_plural = u'游戏平台'
    #图片显示
    def identification(self):
        return '<img src="/media/%s"/  width="50"/ height="50"/ >' % self.img
    identification.allow_tags = True
    identification.short_description = "平台标识"
#游戏配件
class Fittings(models.Model):
    name = models.CharField(u'配件名称',max_length=50)
    enname = models.CharField(u'英文名称',max_length=50)
    created_at = models.DateTimeField(u'创建时间',auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间',auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'游戏配件'
        verbose_name_plural = u'游戏配件'
#游戏内容
#名称、短名称、简介、评分、资源包、容量、推荐配置、浏览数、下载数、排序、推荐、最新、最热、img、img1、img2、img3、img4、img5、支持设备（外健）、游戏类型（外健）
class Game(models.Model):
    name         = models.CharField(u'游戏名称',max_length=30)
    shortname    = models.CharField(u'简称',max_length=5,null=True,blank=True)
    synopsis     = models.TextField(u'概要',null=True,blank=True)

    Genres       = models.ForeignKey("Genres",null=True, verbose_name=u"游戏类型")
    Device       = models.ForeignKey("Device",null=True,verbose_name=u"支持平台")
    Fittings     = models.ManyToManyField("Fittings",verbose_name=u'游戏配件')

    # gamecover    = models.ImageField(u'封面', upload_to='./game/cover/%Y/%m/%d',null=True)

    gamecover = ThumbnailerImageField(u'封面', upload_to='./game/cover/%Y/%m/%d', blank=True)


    score        = models.FloatField(u'评分',null=True)



    # filepath     = models.FileField(u'资源包',upload_to = './game/file/%Y/%m/%d')

    filepath     = models.OneToOneField(File, null=True, verbose_name=u'游戏资源包', unique=True,limit_choices_to={'folder_id': 15})



    filecapacity = models.FloatField(u'容量大小',null=True,blank=True)
    viewingcount = models.IntegerField(u'浏览数',default=0,null=True,blank=True)
    downloadcount= models.IntegerField(u'下载数',default=0,null=True,blank=True)
    playcount    = models.IntegerField(u'打开数',default=0,null=True,blank=True) #edit
    config = models.TextField(u'推荐配置')
    sorting      = models.IntegerField(u'排序',default=255)
    is_free      = models.NullBooleanField(u'免费',default=True,null=True,blank=True)
    price        = models.IntegerField(u'价格', default=0, null=True, blank=True)
    #in_index     = models.BooleanField(u'')
    is_recommend = models.BooleanField(u'推荐',blank=True,default=False)
    is_latest    = models.BooleanField(u'最新',blank=True,default=False)
    is_hottest   = models.BooleanField(u'最热',blank=True,default=False)
    language_choices = (
        (0, u'英语'),
        (1, u'中文'),
        (2, u'其它'),
    )
    language          = models.IntegerField(u'游戏语言',null=True,choices=language_choices)
    productioncompany = models.CharField(u'制作公司',max_length=100,null=True,blank=True)
    publisherofficial = models.CharField(u'发行公司',max_length=100,null=True,blank=True)
    homePage          = models.URLField(u'官方主页',max_length=255,null=True,blank=True)
    rrleasedate       = models.DateTimeField(u'发售日期',null=True,blank=True)
    label             = models.CharField(u'标签',max_length=255,null=True,blank=True)
    forum             = models.URLField(u'讨论区',null=True,blank=True)
    img          = models.ImageField(u'主图', upload_to='./game/img/%Y/%m/%d', blank=True,null=True)
    img1         = models.ImageField(u'图1', upload_to='./game/img1/%Y/%m/%d', blank=True, null=True)
    img2         = models.ImageField(u'图2', upload_to='./game/img2/%Y/%m/%d', blank=True, null=True)
    img3         = models.ImageField(u'图3', upload_to='./game/img3/%Y/%m/%d', blank=True, null=True)
    img4         = models.ImageField(u'图4', upload_to='./game/img4/%Y/%m/%d', blank=True, null=True)
    img5         = models.ImageField(u'图5', upload_to='./game/img5/%Y/%m/%d', blank=True, null=True)

    created_at   = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at   = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
       return u"%s" % self.name
    # def get_device(self):
    #     return "\n".join([p.game_device.name for p in self.Device.all()])
    #封面图片
    def cover(self):
        return '<img src="/media/%s"/  width="150"/ height="85"/ >' % self.gamecover
    cover.allow_tags = True
    cover.short_description = "游戏封面"
    class Meta:
        ordering = ("created_at","updated_at","score","sorting")
        verbose_name = u'游戏内容'
        verbose_name_plural = u'游戏内容'

#----------------------------------------视频管理----------------------------------------
#视频类型
class VideoGenres(models.Model):
    name = models.CharField(u'类型名称', max_length=30)
    shortname = models.CharField(u'简称', max_length=10, default=None)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'视频类型'
        verbose_name_plural = u'视频类型'
#视频分类
class VideoSort(models.Model):
    name = models.CharField(u'分类名称',max_length=30)
    shortname = models.CharField(u'简称',max_length=10,default=None)
    enname = models.CharField(u'英文名',max_length=30,default=None)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'视频分类'
        verbose_name_plural = u'视频分类'
#视频内容
class Video(models.Model):
    name = models.CharField(u'视频名称',max_length=70)
    shortname   = models.CharField(u'简称', max_length=14, default=None,blank=True)
    synopsis    = models.TextField(u'概要',null=True,blank=True)

    starring    = models.CharField(u'主演',max_length=250,null=True,blank=True)

    # videocover  = models.ImageField(u'封面', upload_to='./video/cover/%Y/%m/%d')
    videocover  = ThumbnailerImageField(u'封面',upload_to='./video/cover/%Y/%m/%d',blank=True)
    # Img = ThumbnailerImageField(upload_to='images/', blank=True)

    #videopath   = models.FileField(u'视频文件', upload_to='./video/file/%Y/%m/%d',blank=True)
    videopath = models.OneToOneField(File, null=True, verbose_name=u'视频文件', unique=True,limit_choices_to={'folder_id': 16})

    videourl    = models.URLField(u'视频地址',null=True,blank=True)
    videotime   = models.IntegerField(u'视频时间',null=True,help_text='单位：分钟')
    Genres      = models.ForeignKey("VideoGenres", null=True, verbose_name=u"视频类型")
    Sort        = models.ManyToManyField("VideoSort",verbose_name=u"视频分类")
    score       = models.FloatField(u'评分', null=True)
    filecapacity = models.FloatField(u'容量大小', null=True)
    viewingcount = models.IntegerField(u'浏览数', default=0, null=True, blank=True)
    downloadcount= models.IntegerField(u'下载数', default=0, null=True, blank=True)
    playcount    = models.IntegerField(u'播放数',null=True,default=0)
    label        = models.CharField(u'标签',max_length=255,null=True,blank=True)
    forum        = models.URLField(u'讨论区',null=True,blank=True)
    img          = models.ImageField(u'主图', upload_to='./video/img/%Y/%m/%d', null=True)
    img1         = models.ImageField(u'图1', upload_to='./video/img1/%Y/%m/%d', blank=True, null=True)
    img2         = models.ImageField(u'图2', upload_to='./video/img2/%Y/%m/%d', blank=True, null=True)
    img3         = models.ImageField(u'图3', upload_to='./video/img3/%Y/%m/%d', blank=True, null=True)
    img4         = models.ImageField(u'图4', upload_to='./video/img4/%Y/%m/%d', blank=True, null=True)
    img5         = models.ImageField(u'图5', upload_to='./video/img5/%Y/%m/%d', blank=True, null=True)
    sorting      = models.IntegerField(u'排序',default=255)
    is_panoramic = models.BooleanField(u'360全景',blank=True,default=False)
    is_copyright = models.BooleanField(u'版权',blank=True,default=False)
    is_recommend = models.BooleanField(u'推荐',blank=True,default=False)
    is_latest    = models.BooleanField(u'最新',blank=True,default=False)
    is_hottest   = models.BooleanField(u'最热',blank=True,default=False)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    #封面图片
    def cover(self):
        return '<img src="/media/%s"/  width="150"/ height="85"/ >' % self.videocover
    cover.allow_tags = True
    cover.short_description = "视频封面"

    class Meta:
        ordering = ('created_at',)
        verbose_name = u'视频内容'
        verbose_name_plural = u'视频内容'

# ----------------------------------------图片管理----------------------------------------
# 图片类型
class ImageGenres(models.Model):
    name = models.CharField(u'类型名称', max_length=30)

    shortname = models.CharField(u'简称', max_length=10, default=None)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'图片类型'
        verbose_name_plural = u'图片类型'
# 图片分类
class ImageSort(models.Model):
    name = models.CharField(u'分类名称', max_length=30,unique=True)

    shortname = models.CharField(u'简称', max_length=10, default=None,unique=True)
    folder_id = models.CharField(u'文件夹ID',max_length=100,default=0)
    enname = models.CharField(u'英文名', max_length=30, default=None,unique=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'图片分类'
        verbose_name_plural = u'图片分类'

    def save(self,*args,**kwargs):
        Folder.objects.get_or_create(name=self.name, parent_id=3)
        folder_id = Folder.objects.values_list('id').get(name=self.name)
        self.folder_id = list(folder_id)[0]
        super(ImageSort, self).save(*args, **kwargs)

# 图片内容
class Image(models.Model):
    name = models.CharField(u'图片名称', max_length=249)

    Genres = models.ForeignKey("ImageGenres", null=True, verbose_name=u"图片类型")
    Sort   = models.ForeignKey("ImageSort", verbose_name=u"图片分类",null=True)
    imageurl = models.OneToOneField(File, null=True, verbose_name=u'图片网址文件')
    #imageurl = models.ForeignKey(File,null=True, verbose_name=u'图片网址文件', unique=True)
    synopsis = models.TextField(u'概要', null=True)
    score = models.FloatField(u'评分', null=True)
    playcount = models.IntegerField(u'播放数', null=True)
    sorting = models.IntegerField(u'排序', default=255)
    is_recommend = models.BooleanField(u'推荐', blank=True, default=False)
    is_latest = models.BooleanField(u'最新', blank=True, default=False)
    is_hottest = models.BooleanField(u'最热', blank=True, default=False)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'图片内容'
        verbose_name_plural = u'图片内容'


#----------------------------------------应用管理-----------------------------------------
#应用类型
class AppGenres(models.Model):
    name       = models.CharField(u'类型名称', max_length=30)
    shortname  = models.CharField(u'简称', max_length=10, default=None)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        ordering = ('created_at',)
        verbose_name = u'应用类型'
        verbose_name_plural = u'应用类型'
#应用内容
class App(models.Model):
    name      = models.CharField(u'应用名称', max_length=70)
    shortname = models.CharField(u'简称', max_length=14, default=None, blank=True)
    synopsis  = models.TextField(u'概要', null=True, blank=True)
    appcover  = models.ImageField(u'封面', upload_to='./app/cover/%Y/%m/%d')
    # apppath   = models.FileField(u'应用文件', upload_to='./app/file/%Y/%m/%d')
    apppath   = models.OneToOneField(File, null=True, verbose_name=u'应用文件', unique=True,
                                    limit_choices_to={'folder_id': 17})
    score        = models.FloatField(u'评分', null=True)
    filecapacity = models.FloatField(u'容量大小', null=True, blank=True)
    viewingcount = models.IntegerField(u'浏览数', default=0, null=True, blank=True)
    downloadcount = models.IntegerField(u'下载数', default=0, null=True, blank=True)
    label = models.CharField(u'标签', max_length=255, null=True, blank=True)
    img          = models.ImageField(u'主图', upload_to='./app/img/%Y/%m/%d', null=True)
    img1         = models.ImageField(u'图1', upload_to='./app/img1/%Y/%m/%d', blank=True, null=True)
    img2         = models.ImageField(u'图2', upload_to='./app/img2/%Y/%m/%d', blank=True, null=True)
    img3         = models.ImageField(u'图3', upload_to='./app/img3/%Y/%m/%d', blank=True, null=True)
    img4         = models.ImageField(u'图4', upload_to='./app/img4/%Y/%m/%d', blank=True, null=True)
    img5         = models.ImageField(u'图5', upload_to='./app/img5/%Y/%m/%d', blank=True, null=True)
    sorting      = models.IntegerField(u'排序',default=255)
    is_recommend = models.BooleanField(u'推荐',blank=True,default=False)
    is_latest    = models.BooleanField(u'最新',blank=True,default=False)
    is_hottest   = models.BooleanField(u'最热',blank=True,default=False)
    Genres     = models.ForeignKey("AppGenres", null=True, verbose_name=u"应用类型")
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    #封面图片
    def cover(self):
        return '<img src="/media/%s"/  width="150"/ height="85"/ >' % self.appcover
    cover.allow_tags = True
    cover.short_description = "应用封面"
    class Meta:
        ordering = ('created_at','sorting',)
        verbose_name = u'应用内容'
        verbose_name_plural = u'应用内容'

#----------------------------------------评论管理-----------------------------------------
class Topic(models.Model):
    # from_uid     = models.ForeignKey("User", verbose_name=u"来源用户")
    # from_game    = models.ForeignKey("Game", verbose_name=u"来源游戏主题")

    from_uid_id  = models.IntegerField(verbose_name=u"来源用户",null=True)
    from_game_id = models.IntegerField(verbose_name=u"来源游戏主题",null=True)
    content      = models.TextField(u'评论内容')
    is_top       = models.NullBooleanField(u'置顶',blank=True)
    created_at   = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at   = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.id
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'游戏用户评论'
        verbose_name_plural = u'游戏用户评论'
class VideoTopic(models.Model):
    from_uid_id  = models.IntegerField(verbose_name=u"来源用户",null=True)
    from_video_id = models.IntegerField(verbose_name=u"来源游戏主题",null=True)
    content = models.TextField(u'评论内容')
    is_top = models.NullBooleanField(u'置顶', blank=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.id
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'视频用户评论'
        verbose_name_plural = u'视频用户评论'
class AppTopic(models.Model):
    from_uid_id  = models.IntegerField(verbose_name=u"来源用户",null=True)
    from_app_id  = models.IntegerField(verbose_name=u"来源游戏主题",null=True)
    content = models.TextField(u'评论内容')
    is_top = models.NullBooleanField(u'置顶', blank=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.id
    class Meta:
        ordering = ('created_at',)
        verbose_name = u'应用用户评论'
        verbose_name_plural = u'应用用户评论'

#----------------------------------------广告资源位置管理-----------------------------------
class Ad(models.Model):
    local_choice  = (
        (1, u'精选'),
        (2, u'影视'),
        (3, u'图片'),
        (4, u'游戏'),
        (5, u'直播'),
        (6, u'其它'),
    )

    local      = models.IntegerField(u'资源位置',choices=local_choice)
    ad_img     = models.ImageField(u'资源图',upload_to='./Ad/img/%Y/%m/%d')
    title      = models.CharField(u'标题',max_length=255,null=True,blank=True,default='zzz')
    score      = models.IntegerField(u'评分',null=True,blank=True)

    sorting    = models.IntegerField(u'排序', default=255,blank=True)

    #to        = models.IntegerField(u'资源',default=0)
    ad_url     = models.URLField(u"网址",blank=True,null=True)
    clickcount = models.IntegerField(u'点击数', default=0,blank=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.id

    def cover(self):
        return '<img src="/media/%s"/  width="150"/ height="85"/ >' % self.ad_img
    cover.allow_tags = True
    cover.short_description = "广告图"

    class Meta:
        ordering = ('created_at',)
        verbose_name = u'广告资源'
        verbose_name_plural = u'广告资源'
#----------------------------------------软件升级包管理-------------------------------------
#VR助手包(软件)
class AppUpdateMessage(models.Model):
    APP_CODE = models.CharField(u'软件包id', max_length=50,blank=True)
    APP_ID_choice=(
        (0, 'windows'),
        (1, 'android'),
        (2, 'ios'),
    )
    APP_ID              = models.IntegerField(u'appId',choices=APP_ID_choice)
    APP_NAME            = models.CharField(u'软件包名',max_length=50,blank=True)
    VERSION_MILEPOST_choice = (
        (0, u'是'),
        (1, u'否'),
    )
    VERSION_MILEPOST    = models.IntegerField(u'里程牌',choices=VERSION_MILEPOST_choice,blank=True,default=1)
    VERSION_CODE        = models.CharField(u'版本号',max_length=50,unique=True)
    VERSION_CODE_BEFORE = models.CharField(u'上一个版本号',max_length=50,blank=True)
    VERSION_TYPE_choice = (
        (0, u'选择更新'),
        (1, u'强制更新'),
    )
    VERSION_TYPE        = models.IntegerField(u'版本类型',choices=VERSION_TYPE_choice)
    #APPFilePath= FileStorage()
    #APPFilePath.filetype = "software"
    #DOWNLOAD_PATH       =models.FileField(u'资源文件',storage=APPFilePath,null=True)
    DOWNLOAD_PATH       = models.OneToOneField(File, null=True, verbose_name=u'资源文件',unique=True,limit_choices_to = {'folder_id': 2})
    # DOWNLOAD_URL        =models.CharField(u'下载地址',max_length=500,null=True)
    # DOWNLOAD_URL_COUNT  =models.IntegerField(u'下载更新次数',default=0,blank=True,null=True)
    # VERSION_BIG         =models.CharField(u'新版本大小(kb)', max_length=100,blank=True,null=True,default=0)
    # VERSION_MD5         =models.CharField(u'文件MD5',max_length=500,blank=True,default=0)
    UPDATE_TITLE_CN     = models.CharField(u'升级信息简要(中文)',max_length=50)
    UPDATE_TITLE_EN     = models.CharField(u'升级信息简要(英文)',max_length=50)
    UPDATE_MESSAGE_CN   = models.TextField(u'升级信息详情(中文)',max_length=1000)
    UPDATE_MESSAGE_EN   = models.TextField(u'升级信息详情(英文)',max_length=1000)
    CREATED_AT          = models.DateTimeField(u'创建时间', auto_now_add=True)
    UPDATED_AT          = models.DateTimeField(u'更新时间', auto_now=True)
    STATUS_choice = (
        (0, u'发布版本'),
        (1, u'历史版本'),
    )
    STATUS              = models.IntegerField(u'版本状态',choices=STATUS_choice,default=0)
    UPDATE_PARAMS       = models.CharField(u'添加扩展',max_length=50,null=True,blank=True)
    def __unicode__(self):
        # BIG = AppUpdateMessage.objects.get(id=self.id)
        # VFileMd5 = FileMd5("isfile",self.DOWNLOAD_PATH.path)
        # BIG.VERSION_MD5  =VFileMd5.md5sum()
        # BIG.DOWNLOAD_URL =self.DOWNLOAD_PATH
        # BIG.save()  # 保存
        return u"%s" % self.APP_NAME
    def save(self, *args, **kwargs):
        #self.VERSION_BIG = self.DOWNLOAD_PATH.size/1024
        #self.DOWNLOAD_URL = HttpRequest.get_host()
        super(AppUpdateMessage, self).save(*args, **kwargs)  # Call the "real" save() method.

    # def toJSON(self):
    #     fields = []
    #     for field in self._meta.fields:
    #         fields.append(field.name)
    #     d = {}
    #     for attr in fields:
    #         if isinstance(getattr(self, attr), datetime.):
    #             d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
    #         elif isinstance(getattr(self, attr), datetime.date):
    #             d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
    #         else:
    #             d[attr] = getattr(self, attr)
    #     import json
    #     return json.dumps(d)

    class Meta:
        ordering = ('CREATED_AT',)
        verbose_name = u'VR助手升级包'
        verbose_name_plural = u'VR助手升级包'
#固件厂商ID
class ManuFactor(models.Model):
    CN_NAME    = models.CharField(u'厂商中文名',max_length=50)
    EN_NAME    = models.CharField(u'厂商英文名',max_length=50)
    LOGO_PATH  = models.OneToOneField(File, null=True, verbose_name=u'LOGO ID',unique=True,limit_choices_to = {'folder_id': 5},help_text='文件管理器')
    CREATED_AT = models.DateTimeField(u'创建时间', auto_now_add=True)
    UPDATED_AT = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.CN_NAME

    def cover(self):
        aa = File.objects.values('file').filter(id=self.LOGO_PATH_id)[0]['file']
        return '<img src="/media/%s"/  width="150"/ height="85"/ >' % aa

    cover.allow_tags = True
    cover.short_description = "广告图"
    #def get_file(self):
    #return "\n".join([p.file for p in File.objects.all()])
    class Meta:
        ordering = ('CREATED_AT',)
        unique_together = ('CN_NAME', 'EN_NAME',)
        verbose_name = u'固件厂商'
        verbose_name_plural = u'固件厂商'
#固件类型
class FWareType(models.Model):
    CN_NAME = models.CharField(u'类型中文名',max_length=50) 
    EN_NAME = models.CharField(u'类型英文名',max_length=50)
    CREATED_AT = models.DateTimeField(u'创建时间', auto_now_add=True)
    UPDATED_AT = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return u"%s" % self.CN_NAME
    class Meta:
        ordering = ('CREATED_AT',)
        unique_together = ('CN_NAME','EN_NAME',)
        verbose_name = u'固件类型'
        verbose_name_plural = u'固件类型'
#固件升级包
class FirmWareUpdateMessage(models.Model):
     # DOWNLOAD_PATH_TEST = models.ForeignKey(File,null=True,verbose_name=u'测试')
     FIRMWARE_NAME = models.CharField(u'固件包名', max_length=50,null=True)
     ManuFactor = models.ForeignKey("ManuFactor", null=True, verbose_name=u"固件厂商")
     FirmWare   = models.ForeignKey("FWareType", null=True, verbose_name=u"固件类型")
     VERSION_CODE = models.CharField(u'版本号', max_length=50,unique=True)
     VERSION_TYPE_choice = (
        (0, u'选择更新'),
        (1, u'强制更新'),
     )
     VERSION_TYPE = models.IntegerField(u'版本类型', choices=VERSION_TYPE_choice)
     IS_SILENCE_choice = (
         (0, u'后台升级'),
         (1, u'提醒升级'),
     )
     IS_SILENCE   = models.IntegerField(u'静默升级',choices=IS_SILENCE_choice)
     #FirmWareFilePath = FileStorage()
     #FirmWareFilePath.filetype = "firmware"
     #DOWNLOAD_PATH= models.FileField(u'资源文件', storage=FirmWareFilePath,null=True)
     DOWNLOAD_PATH = models.OneToOneField(File, null=True, verbose_name=u'资源文件',unique=True,limit_choices_to = {'folder_id': 1})
     #DOWNLOAD_URL = models.CharField(u'下载地址',max_length=500,null=True)
     #DOWNLOAD_URL_COUNT = models.IntegerField(u'下载更新次数', default=0, blank=True, null=True)
     #VERSION_BIG = models.CharField(u'新版本大小(kb)', max_length=100, blank=True, null=True, default=0)
     #VERSION_MD5 = models.CharField(u'文件MD5', max_length=500, blank=True, default=0)
     UPDATE_TITLE_CN = models.CharField(u'升级信息简要(中文)', max_length=50)
     UPDATE_TITLE_EN = models.CharField(u'升级信息简要(英文)', max_length=50)
     UPDATE_MESSAGE_CN = models.TextField(u'升级信息详情(中文)', max_length=1000)
     UPDATE_MESSAGE_EN = models.TextField(u'升级信息详情(英文)', max_length=1000)
     CREATED_AT = models.DateTimeField(u'创建时间', auto_now_add=True)
     UPDATED_AT = models.DateTimeField(u'更新时间', auto_now=True)
     def __unicode__(self):
         # BIG = FirmWareUpdateMessage.objects.get(id=self.id)
         # VFileMd5 = FileMd5("isfile", self.DOWNLOAD_PATH.path)
         # BIG.VERSION_MD5 = VFileMd5.md5sum()
         # BIG.DOWNLOAD_URL = self.DOWNLOAD_PATH
         # BIG.save()  # 保存
         return u"%s" % self.FIRMWARE_NAME
     def save(self, *args, **kwargs):
            # self.VERSION_BIG  = self.DOWNLOAD_PATH.size / 1024
            # self.VERSION_MD5  = File.sha1
            #self.DOWNLOAD_URL = HttpRequest.get_host
            super(FirmWareUpdateMessage, self).save(*args, **kwargs)  # Call the "real" save() method.
     class Meta:
         ordering = ('CREATED_AT',)
         verbose_name = u'固件升级包'
         verbose_name_plural = u'固件升级包'


#------------------------------------------------------------------#
class users(models.Model):
    name            = models.CharField(u'用户名',max_length=255)
    email           = models.CharField(u'电子邮箱',max_length=255)
    remember_token  = models.CharField(max_length=100)
    created_at      = models.DateTimeField(u'创建时间',auto_now_add=True)
    updated_at      = models.DateTimeField(u'更新时间',auto_now=True)
    avatars         = models.CharField(u'头像',max_length=30)
    tel             = models.CharField(u'电话号码',max_length=20)
    jobnumber       = models.IntegerField(u'工号')
    truename        = models.CharField(u'真实姓名',max_length=30)
    sex             = models.IntegerField(u'性别',)
    department      = models.CharField(u'入职部门',max_length=20)
    hiretime        = models.CharField(u'入职时间',max_length=20)
    logintime       = models.DateTimeField(u'登录时间',auto_now=True)
    loginip         = models.CharField(u'登录IP',max_length=20)
    class Mate:
        ordering = ('created_at',)

class Snippet(models.Model):
    created  = models.DateTimeField(auto_now_add=True)
    title    = models.CharField(max_length=100, blank=True, default='')
    code     = models.TextField()
    linenos  = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style    = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    class Meta:
        ordering = ('created',)