#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: Julian
@license: Apache Licence 
@contact: aqkt_436@163.com
@site: http://www.abbstyle.com
@software: PyCharm
@time: 2017/4/20 11:00
"""
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from CMS.models import Topic,VideoTopic,AppTopic
from CMSAPI.serializers import *
from rest_framework import status


class GameTopic(APIView):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            game_topic_list = Topic.objects.all().order_by('created_at')
            game_topic_seri = GametopicSerializer(game_topic_list,many=True)
            result = {"result":{"game":game_topic_seri.data}}
            return Response(result)

    def post(self,request, *args, **kwargs):
        if request.method == "POST":
            if request.user.is_authenticated():
                serializer = GametopicSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                from_uid_id = serializer.validated_data['from_uid_id']
                from_game_id = serializer.validated_data['from_game_id']
                content = serializer.validated_data['content']
                result = Topic.objects.create(from_uid_id=from_uid_id,from_game_id=from_game_id,content=content)
                if result:
                    return Response({"result":"success"})
                else:
                    Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

class GameTopicDetail(APIView):
    def get_object(self,id):
        try:
            return Topic.objects.get(id=id)
        except Topic.DoesNotExist:
            raise Http404
    def get(self,request,id,format=None):
        topic  = self.get_object(id)
        serializer = GametopicSerializer(topic)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        topic   = self.get_object(id)
        serializer = GametopicSerializer(topic,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        if request.user.is_authenticated():
            topic = self.get_object(id)
            topic.delete()
            return Response({"result":"success"})
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class Video_Topic(APIView):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            video_topic_list =VideoTopic.objects.all().order_by('created_at')
            video_topic_seri = VideotopicSerializer(video_topic_list,many=True)
            result = {"result":{"video":video_topic_seri.data}}
            return Response(result)
    #
    def post(self,request, *args, **kwargs):
        if request.method == "POST":
            if request.user.is_authenticated():
                serializer = VideotopicSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                from_uid_id = serializer.validated_data['from_uid_id']
                from_video_id = serializer.validated_data['from_video_id']
                content = serializer.validated_data['content']
                result = VideoTopic.objects.create(from_uid_id=from_uid_id,from_video_id=from_video_id,content=content)
                if result:
                    return Response({"result":"success"})
                else:
                    Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

class VideoTopicDetail(APIView):
    def get_object(self,id):
        try:
            return VideoTopic.objects.get(id=id)
        except VideoTopic.DoesNotExist:
            raise Http404
    def get(self,request,id,format=None):
        topic  = self.get_object(id)
        serializer = VideotopicSerializer(topic)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        topic   = self.get_object(id)
        serializer = VideotopicSerializer(topic,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        if request.user.is_authenticated():
            topic = self.get_object(id)
            topic.delete()
            return Response({"result":"success"})
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

class APP_Topic(APIView):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            app_topic_list =AppTopic.objects.all().order_by('created_at')
            app_topic_seri = ApptopicSerializer(app_topic_list,many=True)
            result = {"result":{"app":app_topic_seri.data}}
            return Response(result)
    #
    def post(self,request, *args, **kwargs):
        if request.method == "POST":
            if request.user.is_authenticated():
                serializer = ApptopicSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                from_uid_id = serializer.validated_data['from_uid_id']
                from_app_id = serializer.validated_data['from_app_id']
                content = serializer.validated_data['content']
                result = AppTopic.objects.create(from_uid_id=from_uid_id,from_app_id=from_app_id,content=content)
                if result:
                    return Response({"result":"success"})
                else:
                    Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

class AppTopicDetail(APIView):
    def get_object(self,id):
        try:
            return AppTopic.objects.get(id=id)
        except AppTopic.DoesNotExist:
            raise Http404
    def get(self,request,id,format=None):
        topic  = self.get_object(id)
        serializer = ApptopicSerializer(topic)
        return Response(serializer.data)
    def put(self,request,id,format=None):
        topic   = self.get_object(id)
        serializer = ApptopicSerializer(topic,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        if request.user.is_authenticated():
            topic = self.get_object(id)
            topic.delete()
            return Response({"result":"success"})
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

Game_Topic = GameTopic.as_view()
Game_Topic_Detail = GameTopicDetail.as_view()

Video_Topic = Video_Topic.as_view()
Video_Topic_Detail = VideoTopicDetail.as_view()

App_Topic = APP_Topic.as_view()
App_Topic_Detail = AppTopicDetail.as_view()