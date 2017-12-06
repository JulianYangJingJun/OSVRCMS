# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User as U, Group
#from rest_framework.authtoken.views import ObtainAuthToken
from CMS.models import Game
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from CMSAPI.serializers import *
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token



class UserViewSet(viewsets.ModelViewSet):
    queryset = U.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class topicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = GametopicSerializer

class VideotopicViewSet(viewsets.ModelViewSet):
    queryset = VideoTopic.objects.all()
    serializer_class = VideotopicSerializer

class ApptopicViewSet(viewsets.ModelViewSet):
    queryset = AppTopic.objects.all()
    serializer_class = ApptopicSerializer
# class GameViewSet(viewsets.ModelViewSet):#游戏列表
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer
#
# class Game_freeViewSet(viewsets.ModelViewSet):
#     queryset = Game.objects.filter(is_free=True)
#     serializer_class = GameSerializer
@api_view(['POST'])
def TEST(request):
    if request.user.is_authenticated()==False:
        return  Response(1)
    elif request.user.is_authenticated()==True:
        return Response(2)

@api_view(['GET'])#1、是否是推荐（综合）
def recommends(request,type=None,sort_type=None,format=None):
    if request.method == "GET":
            if sort_type == None:
                order = "updated_at"
            elif sort_type == "up":
                order = "-sorting"
            elif sort_type == "down":
                order = "sorting"
            else:
                order = "sorting"
            if type == None:
                game_list   = Game.objects.filter(is_recommend=True).order_by(order)[:10]
                video_list  = Video.objects.filter(is_recommend=True).order_by(order)[:10]
                app_list    = App.objects.filter(is_recommend=True).order_by(order)[:10]
                game_seri   = GameSerializer(game_list, many=True)
                video_Seri  = VideoSerializer(video_list, many=True)
                app_Seri    = AppSerializer(app_list, many=True)
                result = {"result":{"game":game_seri.data,"video":video_Seri.data,"app":app_Seri.data}}
            elif type == "game":
                game_list = Game.objects.filter(is_recommend=True).order_by(order)[:10]
                game_seri = GameSerializer(game_list, many=True)
                result = {"result": {"game": game_seri.data}}
            elif type == "video":
                video_list = Video.objects.filter(is_recommend=True).order_by(order)[:10]
                video_Seri = VideoSerializer(video_list, many=True)
                result = {"result": {"video": video_Seri.data}}
            elif type == "app":
                app_list = App.objects.filter(is_recommend=True).order_by(order)[:10]
                app_Seri = AppSerializer(app_list, many=True)
                result = {"result": {"app": app_Seri.data}}
            else:
               return  Response(status=status.HTTP_404_NOT_FOUND)
            return Response(result)

@api_view(['GET'])#2、获取下载量最多的游戏(最火的游戏)
def game_hottest(request,format=None):
    if request.method == "GET":
       game_list = Game.objects.filter(is_hottest=True).order_by("-downloadcount")
       serializer = GameSerializer(game_list, many=True)
       return Response(serializer.data)

@api_view(['GET'])#3、获取评分最高的内容（综合）
def highest_marks(request,type=None,sort_type=None,format=None):
    if request.method == "GET":
        if sort_type == None:
            order = "updated_at"
        elif sort_type == "up":
            order = "-score"
        elif sort_type == "down":
            order = "score"
        else:
            order = "score"
        if type == None:
            game_list   = Game.objects.filter(is_recommend=True).order_by(order)[:10]
            video_list  = Video.objects.filter(is_recommend=True).order_by(order)[:10]
            app_list    = App.objects.filter(is_recommend=True).order_by(order)[:10]
            game_seri   = GameSerializer(game_list, many=True)
            video_Seri  = VideoSerializer(video_list, many=True)
            app_Seri    = AppSerializer(app_list, many=True)
            result = {"result":{"game":game_seri.data,"video":video_Seri.data,"app":app_Seri.data}}
        elif type == "game":
            game_list = Game.objects.filter(is_recommend=True).order_by(order)[:10]
            game_seri = GameSerializer(game_list, many=True)
            result = {"result": {"game": game_seri.data}}
        elif type == "video":
            video_list = Video.objects.filter(is_recommend=True).order_by(order)[:10]
            video_Seri = VideoSerializer(video_list, many=True)
            result = {"result": {"video": video_Seri.data}}
        elif type == "app":
            app_list = App.objects.filter(is_recommend=True).order_by(order)[:10]
            app_Seri = AppSerializer(app_list, many=True)
            result = {"result": {"app": app_Seri.data}}
        else:
           return  Response(status=status.HTTP_404_NOT_FOUND)
        return Response(result)

@api_view(['GET']) #4、免费游戏
def game_free(request,format=None):
    if request.method == 'GET':
       game_list = Game.objects.filter(is_free=True)
       if len(game_list):
           serializer = GameSerializer(game_list, many=True)
           result = {"result":serializer.data}
           return Response(result)
       else:
           result ={ "result":{ "error": "no data in free game"} }
           return Response(result)
#-------------------------------
@api_view(['GET']) #5、广告资源
def ad_list(request,format=None):
    if request.method == "GET":
            ad_list = Ad.objects.all()
            serializer = AdSerializer(ad_list,many=True)
            return Response(serializer.data)
@api_view(['GET'])
def ad_detail(request,id,format=None):    #广告资源详情
    try:
        ad_detail = Ad.objects.filter(local=id)
    except Ad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AdSerializer(ad_detail,many=True)
        return Response(serializer.data)


@api_view(['GET'])#6、最新内容（综合）
def lastest(request,type=None,sort_type=None,format=None):
    if request.method == "GET":
        if sort_type == None:
            order = "created_at"
        elif sort_type == "up":
            order = "-created_at"
        elif sort_type == "down":
            order = "created_at"
        else:
            order = "created_at"
        if type == None:
            game_list   = Game.objects.all().order_by(order)[:10]
            video_list  = Video.objects.all().order_by(order)[:10]
            app_list    = App.objects.all().order_by(order)[:10]
            game_seri   = GameSerializer(game_list, many=True)
            video_Seri  = VideoSerializer(video_list, many=True)
            app_Seri    = AppSerializer(app_list, many=True)
            result = {"result":{"game":game_seri.data,"video":video_Seri.data,"app":app_Seri.data}}
        elif type == "game":
            game_list = Game.objects.filter(is_recommend=True).order_by(order)[:10]
            game_seri = GameSerializer(game_list, many=True)
            result = {"result": {"game": game_seri.data}}
        elif type == "video":
            video_list = Video.objects.filter(is_recommend=True).order_by(order)[:10]
            video_Seri = VideoSerializer(video_list, many=True)
            result = {"result": {"video": video_Seri.data}}
        elif type == "app":
            app_list = App.objects.filter(is_recommend=True).order_by(order)[:10]
            app_Seri = AppSerializer(app_list, many=True)
            result = {"result": {"app": app_Seri.data}}
        else:
           return  Response(status=status.HTTP_404_NOT_FOUND)
        return Response(result)




# @api_view(['GET','POST'])
# def marks_game(request,format=None):
#     if request.method == "GET":









#详情---------------------------------------------------------
#游戏
@api_view(['GET'])
def game(reqeust,format=None):               #游戏列表
    if reqeust.method == "GET":
        game_list = Game.objects.all()
        serializer= GameSerializer(game_list,many=True)
        result = {'result':serializer.data}
        return Response(result)
@api_view(['GET'])
def game_detail(request,pk,format = None):   #游戏详情
    try:
        game_detail = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GameSerializer(game_detail)
        return Response(serializer.data)
@api_view(['GET'])
def video_detail(request,pk,format = None):   #视频详情
    try:
        Video_detail = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VideoSerializer(Video_detail)
        return Response(serializer.data)
@api_view(['GET'])
def app_detail(request,pk,format = None):   #应用详情
    try:
        App_detail = App.objects.get(pk=pk)
    except App.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AppSerializer(App_detail)
        return Response(serializer.data)

@api_view(['GET'])
def game_download(request, format=None):  # 下载量最多
    if request.method == "GET":
        game_list = Game.objects.all().order_by('-downloadcount')
        serializer = GameSerializer(game_list, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def game_hottest(request,format=None):      #最热游戏
    if request.method == "GET":
       game_list = Game.objects.filter(is_hottest=True).order_by("-downloadcount")
       serializer = GameSerializer(game_list, many=True)
       return Response(serializer.data)

@api_view(['GET'])
def game_highest(reqeust,format=None):      #评份最高的游戏
    if reqeust.method == "GET":
        game_list = Game.objects.all().order_by("-score")
        serializer= GameSerializer(game_list,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def game_recommend(request,format=None):     #推荐的游戏
    if request.method == "GET":
        game_list = Game.objects.filter(is_recommend=True)
        serializer = GameSerializer(game_list, many=True)
        return Response(serializer.data)
