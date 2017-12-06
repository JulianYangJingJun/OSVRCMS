# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#!E:\www\python\OSVRCMS\env python
# @Date    : Date
# @Author  : Julian Yang (aqkt_436@163.com)
# @Link    : http://www.abbstyle.com



from django.contrib import admin
from CMS.models import *
from django import forms
from django.db import models
from CMS.forms import *
from form_utils.widgets import ImageWidget
from django.utils.html import format_html
import os

# User admin list
class UserAdmin(admin.ModelAdmin):

    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}
    list_display = ('avatarss','name', 'email','mobil','ip','created_at','updated_at')# 定义admin总览里每行的显示信息，由于email是在userprofile的外键user表中，所以需要特殊返回，注意这个字段不能用user__email的形式
    search_fields = ('name',) # 定义搜索框以哪些字段可以搜索
    #list_filter = ('name','email')  # 传入的需要是列表，设定过滤列表
    fields = ('name','password','email', 'avatars','mobil','ip')
    form = UserForm

# UserProfile admin list
class UserProfileAdmin(admin.ModelAdmin):
    #pass
    def get_adopt_state(self,obj):
        if obj.adopt == 0:
            return u'<span style="color:red;font-weight:bold">%s</span>' % (u"未审核",)
        elif obj.adopt == 1:
            return u'<span style="color:green;font-weight:bold">%s</span>' % (u"通过",)
        else:
            return u'<span style="color:orange;font-weight:bold">%s</span>' % (u"已通过",)
        # 显示HTML
        # if obj.adopt == 0:
        #     return u'<select name="adopt" id="id_adopt">' \
        #            u'<option value="0" selected="">待审核</option>' \
        #            u'<option value="1">通过</option>' \
        #            u'<option value="2">未通过</option></select>'
        # elif obj.adopt == 1:
        #     return u'<select name="adopt" id="id_adopt">' \
        #            u'<option value="0" >待审核</option>' \
        #            u'<option value="1" selected="">通过</option>' \
        #            u'<option value="2">未通过</option></select>'
        # elif obj.adopt == 2:
        #     return u'<select name="adopt" id="id_adopt">' \
        #            u'<option value="0">待审核</option>' \
        #            u'<option value="1">通过</option>' \
        #            u'<option value="2"  selected="">未通过</option></select>'
    get_adopt_state.short_description = u'审核'
    get_adopt_state.allow_tags = True
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}
    list_display = ('credentialName', 'credentialType', 'credentialPhoto','credentialNum',  'get_adopt_state','created_at','updated_at')
    search_fields = ('credentialName',)
    list_filter = ('adopt',)
    fields = ('credentialName', 'credentialType', 'credentialNum', 'credentialPhoto', 'credentialPhotoBack', 'adopt')
    form = UserProfileForm

















# Device admin list
class DeviceAdmin(admin.ModelAdmin):
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}
    list_display = ('identification','name', 'shortname', 'created_at','updated_at')
    search_fields = ('name','shortname',)
    fields = ('name', 'shortname','img')
    form = DeviceForm

# Genres admin list
class GenresAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'created_at','updated_at')
    search_fields = ('name', 'shortname', 'is_recommend', 'is_latest', 'is_hottest',)
    fields = ('name', 'shortname')
    form = GenresForm

# Fittings admin list
class FittingsAdmin(admin.ModelAdmin):
    list_display = ('name','enname', 'created_at','updated_at')
    search_fields = ('name','ennname')





# Game admin list
class GameAdmin(admin.ModelAdmin):
    sortable = 'sorting'
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}
    Genres.short_description = u"游戏类型"
    list_display = ('cover','name','shortname','score', 'viewingcount', 'downloadcount','is_recommend','is_latest','is_hottest','sorting','Genres','created_at','updated_at')
    search_fields = ('name','shortname',)
    list_editable = ('name','score','viewingcount', 'downloadcount','sorting','is_recommend','is_latest','is_hottest')
    list_filter = ('shortname', 'is_recommend', 'is_latest', 'is_hottest',)
    form = GameForm
















# VideoGenres admin list
class VideoGenresAamin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'created_at','updated_at')
    search_fields = ('name','shortname',)
    fields = ('name', 'shortname')
    #form = GenresForm

# VideoSort admin list
class VideoSortAdmin(admin.ModelAdmin):
    list_display = ('name','shortname','enname','created_at','updated_at')
    search_fields = ('name','shortname','enname')
    fields = ('name','shortname','enname')

# Video admin list
class VideoAdmin(admin.ModelAdmin):
    list_display = ('cover', 'name','score', 'Genres','viewingcount', 'downloadcount','is_recommend','is_latest','is_hottest','sorting','created_at')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}
    search_fields = ('name', 'shortname')
    list_editable = ('name','is_recommend','score', 'is_latest', 'is_hottest', 'sorting','viewingcount', 'downloadcount',)





    form = VideoFrom
    list_filter = ('shortname','Genres','Sort','is_recommend', 'is_latest', 'is_hottest',)
    #fields = ('name', 'shortname')
    # form = GameForm






# VideoGenres admin list
class ImageGenresAamin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'created_at','updated_at')
    search_fields = ('name','shortname',)
    fields = ('name', 'shortname')
    form = GenresForm

# VideoSort admin list
class ImageSortAdmin(admin.ModelAdmin):
    list_display = ('name','shortname','enname','created_at','updated_at')
    search_fields = ('name','shortname','enname')
    fields = ('name','shortname','enname')

# Image admin list
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','Genres','synopsis','score','playcount','is_recommend', 'is_latest', 'is_hottest','created_at','updated_at')
    search_fields = ('name', 'Genres','is_recommend','is_latest','is_hottest')
    list_filter = ('Genres', 'is_recommend', 'is_latest', 'is_hottest')
    #fields = ('name','is_recommend','is_latest','is_hottest')
    # list_editable = ('name',)
    form = ImageForm




















#AppGenres admin list
class AppGenresAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'created_at','updated_at')
    search_fields = ('name','shortname',)
    fields = ('name', 'shortname')
    #form = GenresForm
# App admin list
class AppAdmin(admin.ModelAdmin):
    list_display = ('cover', 'name','shortname','score', 'viewingcount', 'downloadcount',
                    'is_recommend','is_latest',
                    'is_hottest','sorting','Genres','created_at','updated_at')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}
    search_fields = ('name', 'shortname',)
    #form = VideoFrom
    list_filter = ('shortname','is_recommend', 'is_latest', 'is_hottest',)
    #fields = ('name', 'shortname')
    #form = GameForm






















class TopicAdmin(admin.ModelAdmin):
    list_display = ('id','from_uid_id', 'from_game_id','is_top','content','created_at', 'updated_at')
    search_fields = ('content',)
    #fields = ('name', 'shortname')
class VideoTopicAdmin(admin.ModelAdmin):
    list_display = ('id','from_uid_id', 'from_video_id','is_top','content','created_at', 'updated_at')
    search_fields = ('content',)
    #fields = ('name', 'shortname')
class AppTopicAdmin(admin.ModelAdmin):
    list_display = ('id','from_uid_id', 'from_app_id','is_top','content','created_at', 'updated_at')
    search_fields = ('content',)
    #fields = ('name', 'shortname')
class AdCreationForm(AdForm):
     local = forms.CharField(label=(u"ADD"))
class AdChangeForm(AdForm):
     local = forms.CharField(label=(u"CHANGE"))

class AdAdmin(admin.ModelAdmin):
        list_display = ('id','local','cover','title','score','ad_url','clickcount','created_at', 'updated_at')
        search_fields = ('title',)
        list_editable = ('title','score','clickcount','ad_url','score')
        list_select_related = True
        formfield_overrides = {models.ImageField: {'widget': ImageWidget}}


class AppUpdateMessageAdmin(admin.ModelAdmin):
      list_display =('id','APP_ID','APP_NAME','DOWNLOAD_PATH','VERSION_MILEPOST','STATUS','CREATED_AT','UPDATED_AT')
      search_fields = ('UPDATE_TITLE_CN',)
      list_filter = ('VERSION_MILEPOST','VERSION_CODE','APP_ID',)
      # search_fields = ('name', 'shortname', 'is_recommend', 'is_latest', 'is_hottest',)
      form = AppUpdateMessageForm


class FWareTypeAdmin(admin.ModelAdmin):
    list_display = ('id','CN_NAME','EN_NAME','CREATED_AT','UPDATED_AT')
    search_fields = ('CN_NAME','EN_NAME',)

class ManuFactorAdmin(admin.ModelAdmin):
    list_display = ('id','CN_NAME','EN_NAME','cover','CREATED_AT','UPDATED_AT')
    search_fields = ('CN_NAME','EN_NAME',)


class FirmWareUpdateMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'FIRMWARE_NAME', 'ManuFactor', 'FirmWare','VERSION_CODE','DOWNLOAD_PATH','CREATED_AT', 'UPDATED_AT')
    search_fields = ('FIRMWARE_NAME',)
    list_filter = ('VERSION_CODE','IS_SILENCE','ManuFactor','FirmWare')
    # search_fields = ('name', 'shortname', 'is_recommend', 'is_latest', 'is_hottest',)
    form = FirmWareUpdateMessageForm

# class AppHeartAdmin(admin.ModelAdmin):
#     list_display = ('id','APPIP')
#     search_fields = ('APPIP',)



def expiration(obj):
    import datetime
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    exp_time = obj.expiration.strftime('%Y-%m-%d %H:%M:%S')
    if now_time > exp_time:
        return format_html("<img src='/static/admin/img/icon-no.svg' alt='True'>")
    else:
        return format_html("<img src='/static/admin/img/icon-yes.svg' alt='False'>")
def challenge(obj):
    from captcha.helpers import captcha_image_url
    return format_html('<img src='+settings.URL + captcha_image_url(obj.hashkey)+'>')
expiration.short_description = '有效期'
challenge.short_description ='challenge'
class CaptchaAdmin(admin.ModelAdmin):
    list_display = ('id',challenge,'response','hashkey',expiration)
    # list_display_links = ('challenge', 'response')
    # list_display = (upper_case_name,)
    date_hierarchy = 'expiration'


from captcha.models import CaptchaStore
admin.site.register(CaptchaStore,CaptchaAdmin)




# register admin template
# User master
admin.site.register(User,UserAdmin)                                                                                                                    # 引用的固定格式，注册的model和对应的Admin,
admin.site.register(UserProfile,UserProfileAdmin)
# Gamge master
admin.site.register(Genres,GenresAdmin)
admin.site.register(Device,DeviceAdmin)
admin.site.register(Fittings,FittingsAdmin)
admin.site.register(Game,GameAdmin)
# video master
admin.site.register(VideoGenres,VideoGenresAamin)
admin.site.register(VideoSort,VideoSortAdmin)
admin.site.register(Video,VideoAdmin)
#image master
admin.site.register(ImageGenres,ImageGenresAamin)
admin.site.register(ImageSort,ImageSortAdmin)
admin.site.register(Image,ImageAdmin)



#App master
admin.site.register(AppGenres,AppGenresAdmin)
admin.site.register(App,AppAdmin)
#Topic master
admin.site.register(Topic,TopicAdmin)
admin.site.register(VideoTopic,VideoTopicAdmin)
admin.site.register(AppTopic,AppTopicAdmin)
#Ad master
#admin.site.register(Ad,AdAdmin)
admin.site.register(Ad,AdAdmin)


admin.site.register(AppUpdateMessage,AppUpdateMessageAdmin)
admin.site.register(FirmWareUpdateMessage,FirmWareUpdateMessageAdmin)
admin.site.register(FWareType,FWareTypeAdmin)
admin.site.register(ManuFactor,ManuFactorAdmin)
# admin.site.register(AppHeart,AppHeartAdmin)

