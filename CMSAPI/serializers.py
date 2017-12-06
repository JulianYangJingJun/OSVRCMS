# -*- coding: utf-8 -*-
# @Date    : Date
# @Author  : Julian Yang (aqkt_436@163.com)
# @Link    : http://www.abbstyle.com
from django.contrib.auth.models import User as U, Group
from CMS.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = U
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id','name','score','img','is_recommend','sorting','is_free','price','downloadcount','filepath')

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Video
        fields = ('id','name','score','img','is_recommend','sorting')

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ('id','name','score','img','is_recommend','sorting')

class GametopicSerializer(serializers.HyperlinkedModelSerializer):
    content       = serializers.CharField(max_length=1000)
    from_uid_id   = serializers.IntegerField()
    from_game_id  = serializers.IntegerField()
    def create(self, validated_data):
            content = validated_data['content']
            from_uid_id = validated_data['from_uid_id']
            from_game_id = validated_data['from_game_id']
            topic = Topic(content=content,from_game_id=from_game_id,from_uid_id=from_uid_id)
            topic.save()
            return topic
    def destroy(self, instance):
        topic = Topic.objects.get(id=instance.id).delete()
        return topic

    class Meta:
        model = Topic
        fields = ('id', 'content', 'from_uid_id','from_game_id')

class VideotopicSerializer(serializers.HyperlinkedModelSerializer):
    content       = serializers.CharField(max_length=1000)
    from_uid_id   = serializers.IntegerField()
    from_video_id  = serializers.IntegerField()
    def create(self, validated_data):
            content = validated_data['content']
            from_uid_id = validated_data['from_uid_id']
            from_video_id = validated_data['from_game_id']
            topic = VideoTopic(content=content,from_game_id=from_video_id,from_uid_id=from_uid_id)
            topic.save()
            return topic
    def destroy(self, instance):
        topic = VideoTopic.objects.get(id=instance.id).delete()
        return topic

    class Meta:
        model = VideoTopic
        fields = ('id', 'content', 'from_video_id', 'from_uid_id')

class ApptopicSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.CharField(max_length=1000)
    from_uid_id = serializers.IntegerField()
    from_app_id = serializers.IntegerField()

    def create(self, validated_data):
        content = validated_data['content']
        from_uid_id = validated_data['from_uid_id']
        from_app_id = validated_data['from_app_id']
        topic = AppTopic(content=content, from_app_id=from_app_id, from_uid_id=from_uid_id)
        topic.save()
        return topic

    def destroy(self, instance):
        topic = AppTopic.objects.get(id=instance.id).delete()
        return topic

    class Meta:
        model = AppTopic
        fields = ('id', 'content', 'from_app_id', 'from_uid_id')

class AdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'local', 'ad_img', 'sorting', 'ad_url')



class LoginSerializer(serializers.ModelSerializer):
    name     = serializers.CharField(required=False, max_length=1024)
    password = serializers.CharField(required=False, max_length=1024)
    #aaa      = serializers.CharField(required=False, max_length=1024)
    class Meta:
        model = User
        fields = ('id', 'name', 'password')