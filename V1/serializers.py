#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: Julian
@license: Apache Licence 
@contact: aqkt_436@163.com
@site: http://www.abbstyle.com
@software: PyCharm
@file: serializers.py
@time: 2017/6/12 9:48
"""
from django.contrib.auth.models import User as U, Group
from CMS.models import *
from filer.models import *
from statistics.models import AppHeart as s_AppHeart,AppInstall as s_AppInstall
from rest_framework.settings import api_settings
from rest_framework import serializers
from rest_framework.response import Response
import time
from datetime import date, datetime



class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('id','original_filename','file','_file_size','sha1',)

class AppUpdateMessageSerializer(serializers.HyperlinkedModelSerializer):
    FILE_Detail = serializers.SerializerMethodField()
    def get_FILE_Detail(self,AppUpdateMessage):
        File_Model = File.objects.filter(id=AppUpdateMessage.DOWNLOAD_PATH_id)[:1]
        filter_data = list(File_Model.values('id','file', '_file_size', 'sha1','uploaded_at'))
        Result_Data = {}
        if settings.USE_TZ:
            canonical_time = int((filter_data[0]['uploaded_at'] - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())
        else:
            canonical_time = int((filter_data[0]['uploaded_at'] - datetime(1970, 1, 1)).total_seconds())
        url = ''
        if filter_data[0]['file']:
            try:
                url = urlresolvers.reverse('filecanonical', kwargs={
                    'uploaded_at': canonical_time,
                    'file_id': filter_data[0]['id']
                })
            except urlresolvers.NoReverseMatch:
                pass  # No canonical url, return empty string

        #Result_Data['DOWNLOAD_PATH'] =settings.URL+settings.MEDIA_URL+str(filter_data[0]['file'])
        Result_Data['DOWNLOAD_PATH'] =settings.URL + url#settings.URL + "/CMS/" + str(canonical_time) + "/" + str(filter_data[0]['id'])  # settings.URL+settings.MEDIA_URL+str(filter_data[0]['file'])
        Result_Data['VERSION_BIG']   =filter_data[0]['_file_size']
        Result_Data['VERSION_MD5']   =filter_data[0]['sha1']
        return Result_Data
    class Meta:
        model  = AppUpdateMessage
        fields = ('VERSION_CODE',
                  'VERSION_TYPE',
                  'UPDATE_TITLE_CN',
                  'UPDATE_TITLE_EN',
                  'UPDATE_MESSAGE_EN',
                  'UPDATE_MESSAGE_CN',
                  'FILE_Detail',
                  # 'VERSION_BIG',
                  # 'VERSION_MD5',
                  'CREATED_AT',
                  'UPDATED_AT',
                  # 'DOWNLOAD_URL',
                  )

class FirmWareUpdateMessageSerializer(serializers.HyperlinkedModelSerializer):
    # validated_data.get('APPID', instance.APPIP)
    FILE_Detail = serializers.SerializerMethodField()
    FILE_LOGO   = serializers.SerializerMethodField()

    def get_FILE_Detail(self,AppUpdateMessage):
        File_Model = File.objects.filter(id=AppUpdateMessage.DOWNLOAD_PATH_id)[:1]
        filter_data = list(File_Model.values('id','file', '_file_size', 'sha1','uploaded_at'))
        Result_Data = {}
        if settings.USE_TZ:
            canonical_time = int((filter_data[0]['uploaded_at'] - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())
        else:
            canonical_time = int((filter_data[0]['uploaded_at'] - datetime(1970, 1, 1)).total_seconds())
        url = ''
        if filter_data[0]['file']:
            try:
                url = urlresolvers.reverse('filecanonical', kwargs={
                    'uploaded_at': canonical_time,
                    'file_id': filter_data[0]['id']
                })
            except urlresolvers.NoReverseMatch:
                pass  # No canonical url, return empty string

        #Result_Data['DOWNLOAD_PATH'] =settings.URL+settings.MEDIA_URL+str(filter_data[0]['file'])
        Result_Data['DOWNLOAD_PATH'] =settings.URL + url#settings.URL + "/CMS/" + str(canonical_time) + "/" + str(filter_data[0]['id'])  # settings.URL+settings.MEDIA_URL+str(filter_data[0]['file'])
        Result_Data['VERSION_BIG']   =filter_data[0]['_file_size']
        Result_Data['VERSION_MD5']   =filter_data[0]['sha1']
        return Result_Data

    class Meta:
        model = FirmWareUpdateMessage
        fields = ('ManuFactor_id',
                  'FirmWare_id',
                  'VERSION_CODE',
                  'VERSION_TYPE',
                  'IS_SILENCE',
                  'UPDATE_TITLE_CN',
                  'UPDATE_TITLE_EN',
                  'UPDATE_MESSAGE_EN',
                  'UPDATE_MESSAGE_CN',
                  'FILE_Detail',
                  #'VERSION_BIG',
                  #'VERSION_MD5',
                  #'DOWNLOAD_URL'
                  'CREATED_AT',
                  'UPDATED_AT',
                  )

class AppHeartSerializer(serializers.Serializer):
    id         = serializers.IntegerField(read_only=True)
    APPIP      = serializers.CharField(required=False,allow_blank=True,max_length=50)         #IP地址
    MACADDRESS = serializers.CharField(required=False,max_length=50)                          #mac地址
    LOGINTIME  = serializers.CharField(required=False,max_length=32)                          #初次发送时间
    HEARTRATE  = serializers.IntegerField(required=False)                                     #心跳频率
    ONLINETIME = serializers.CharField(required=False, max_length=50)                         #在线时长
    ONFIRST    = serializers.IntegerField(required=False)                                     #心跳频率
    INTERVAL   = serializers.IntegerField(required=False)                                     #心跳间隔(s)
    #CREATED_AT = serializers.DateTimeField(required=True,auto_now_add=True)                  #创建时间
    #UPDATAD_AT = serializers.DateTimeField(required=True,auto_now=True)                      #更新时间

    def create(self, validated_data,instance=None):
        LOGINTIME   = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))

       # ccc  = validated_data.get('MACADDRESS', instance.MACADDRESS)
       # print s_AppHeart.objects.get(MACADDRESS=ccc)

        return s_AppHeart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.APPIP      = validated_data.get('APPID', instance.APPIP)
        instance.MACADDRESS = validated_data.get('MACADDRESS', instance.MACADDRESS)
        #当天心跳时间
        instance.LOGINTIME  = validated_data.get('LOGINTIME', instance.LOGINTIME)
        #instance.LOGINTIME  = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        #初次心跳频率
        instance.HEARTRATE = instance.HEARTRATE + 1
        # else:
        #     instance.LOGINTIME = validated_data.get('LOGINTIME', instance.LOGINTIME)
        #instance.HEARTRATE  = instance.HEARTRATE + 1#validated_data.get('HEARTRATE', instance.HEARTRATE)
        instance.ONLINETIME = validated_data.get('APPID', instance.ONLINETIME)
        instance.save()
        return instance

    class Meta:
        models = s_AppHeart
        fields = ('APPIP','MACADDRESS','LOGINTIME','HEARTRATE','ONLINETIME')

class AppInstallSerializer(serializers.Serializer):
    MACADDRESS = serializers.CharField(required=False, max_length=50)
    def create(self, validated_data,instance=None):
        return s_AppInstall.objects.create(**validated_data)




    # class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = U
#         fields = ('url', 'username', 'email', 'groups')
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model  = Group
#         fields = ('url', 'name')





class VideoSerializer(serializers.HyperlinkedModelSerializer):
    File_URL = serializers.SerializerMethodField()
    Video_Cover = serializers.SerializerMethodField()
    def get_File_URL(self,VideoSerializer):
        from CMS.templatetags.get_file import GetFileUrl
        try:
            return GetFileUrl(VideoSerializer.videopath_id)
        except:
            return settings.URL

    def get_Video_Cover(self,VideoSerializer):
        from easy_thumbnails.files import get_thumbnailer
        thumb_url = get_thumbnailer(VideoSerializer.videocover)['videocover'].url
        return thumb_url

    class Meta:
        model = Video
        fields = ('id','name','Video_Cover','score','File_URL','starring')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    File_URL = serializers.SerializerMethodField()
    Image_Cover= serializers.SerializerMethodField()
    def get_File_URL(self,ImageSerializer):
        from CMS.templatetags.get_file import GetFileUrl
        try:
            # print GetFileUrl(ImageSerializer.imageurl_id,"None")
            # print GetFileUrl(ImageSerializer.imageurl_id)
            return GetFileUrl(ImageSerializer.imageurl_id)
        except:
            return settings.URL

    def get_Image_Cover(self,ImageSerializer):
        from django.shortcuts import get_object_or_404
        try:
            filer_file = get_object_or_404(File, pk=ImageSerializer.imageurl_id, is_public=True)
            from easy_thumbnails.files import get_thumbnailer
            thumb_url = get_thumbnailer(filer_file)['imagecover'].url
        except:
            return "error"

        return settings.URL+thumb_url

    class Meta:
        model = Image
        fields=('id','name','File_URL','Image_Cover')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    File_URL = serializers.SerializerMethodField()
    Game_Cover = serializers.SerializerMethodField()
    def get_Game_Cover(self, VideoSerializer):
        from easy_thumbnails.files import get_thumbnailer
        thumb_url = get_thumbnailer(VideoSerializer.gamecover)['gamecover'].url
        return thumb_url
    def get_File_URL(self, VideoSerializer):
        from CMS.templatetags.get_file import GetFileUrl
        try:
            return GetFileUrl(VideoSerializer.filepath_id)
        except:
            return settings.URL
    class Meta:
        model = Game
        fields = ('id', 'name','synopsis','File_URL','Game_Cover','is_recommend','is_latest','is_hottest')
