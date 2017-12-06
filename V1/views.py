# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User as U, Group
from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from V1.serializers import *
from filer.models import *
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from CMS.models import *
from statistics.models import *
from captcha.models import CaptchaStore

@api_view(['POST'])
def get_image_file_list(request,format=None):
    if request.method == "POST":
        folder_id = ImageSort.objects.values_list('folder_id').get(id=request.POST.get('id_sort'))
        ImageFile_Models = File.objects.filter(folder=list(folder_id)[0])
        ImageFileVersion_Serializer =FileSerializer(ImageFile_Models,many=True)
        return Response(ImageFileVersion_Serializer.data)

@api_view(['GET'])#1、获取最新的软件版本
def AppLastVersion(request,format=None):
    if request.method == "GET":
       AppLastVersion_Models    =  AppUpdateMessage.objects.all().order_by('-CREATED_AT')[:1]
       AppLastVersion_Serializer = AppUpdateMessageSerializer(AppLastVersion_Models, many=True)
       return Response(AppLastVersion_Serializer.data)

@api_view(['POST'])#3、获取最新的固件版本
def FirmWareLastVersion(request,format=None):
    if request.method == "POST":
        try:
            ManuFactor_ID =  int(request.POST.get('mid'))  #厂商ID
            FirmWare_ID   =  int(request.POST.get('fid'))    #固件类型ID
            if ManuFactor_ID and FirmWare_ID:
                FirmWareLastVersion_Models = FirmWareUpdateMessage.objects.filter(ManuFactor_id=ManuFactor_ID,
                                                                                  FirmWare_id=FirmWare_ID).order_by(
                    '-CREATED_AT')[:10]
                FirmWareUpdateMessage_Serializer = FirmWareUpdateMessageSerializer(FirmWareLastVersion_Models,
                                                                                   many=True)
                if FirmWareUpdateMessage_Serializer.data:
                    return Response(FirmWareUpdateMessage_Serializer.data)
                else:
                    Result_Data = {}
                    Result_Data["status"] = 401
                    Result_Data["message"] = "no data"
                    return Response("[]")
            else:
                Result_Data = {}
                Result_Data["status"] = 401
                Result_Data["message"] = "mid or fid is null"
                return Response("[]")
        except ValueError:
            Result_Data = {}
            Result_Data["status"] = 401
            Result_Data["message"] = "no int data"
            return Response("[]")

@api_view(['GET','POST','PUT'])
def AppHeart_list(request):
    if request.method == "GET":
        AppHeartList = AppHeart.objects.all()
        serializer   = AppHeartSerializer(AppHeartList,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = AppHeartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        serializer = AppHeartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def AppHeart_Detail(request,pk):

    try:
        #if pk == '00-00-00-00-00-00':
        #   return Response('[]',status=status.HTTP_400_BAD_REQUEST)
        toDay = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        AppHeartDetail = AppHeart.objects.get(Q(MACADDRESS=pk),Q(LOGINTIME=str(toDay)))
    except AppHeart.DoesNotExist:
        #如果没有数据进行自增
        #获取初次心跳时间
        Result_Data = {}
        Result_Data['MACADDRESS'] = pk
        Result_Data['LOGINTIME']  = str(toDay)
        Result_Data['HEARTRATE'] = 1
        #如果是第一次ONFIRST 为 1
        get_mac_bool = AppHeart.objects.filter(Q(MACADDRESS=pk),Q(ONFIRST=1))
        if list(get_mac_bool):
            Result_Data['ONFIRST'] = 0
        else:
            Result_Data['ONFIRST'] = 1

        serializer = AppHeartSerializer(data=Result_Data)

        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        serializer = AppHeartSerializer(AppHeartDetail,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def inster_AppHeart(form_data):
    serializer = AppHeartSerializer(data=form_data.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

def download(request):
    import json
    import urllib2
    applast = urllib2.urlopen(r'http://osvr-dev.lianluo.com/V1/applast/')
    DOWNLOAD_PATH = json.loads(applast.read())[0]['FILE_Detail']['DOWNLOAD_PATH']
    return render(request, 'download.html', {'DOWNLOAD_PATH': DOWNLOAD_PATH})







    # Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = U.objects.all()
#     serializer_class = UserSerializer
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
# class AppUpdateMessageViewSet(viewsets.ModelViewSet):
#     queryset = AppUpdateMessage.objects.all()
#     serializer_class = AppUpdateMessageSerializer




#
# 验证码
#
@api_view(['GET'])
def create_captcha(request):
    if request.method == "GET":
        from captcha.helpers import captcha_image_url
        hashkey = CaptchaStore.pick()
        to_json_response = {
            'hide_hashkey': hashkey,
            'captcha':'captcha',
            'image_url': settings.URL+captcha_image_url(hashkey)
        }
        return Response(to_json_response)

@api_view(['POST'])
def user_login(request):
    from django.contrib.auth import login,authenticate
    # from rest_framework.authtoken.models import Token
    username  = request.POST.get('username')
    password  = request.POST.get('password')
    captcha   = request.POST.get('captcha')
    hide_hashkey  = request.POST.get('hide_hashkey')
    if captcha is not None:
        try:
            import datetime
            Captcha = CaptchaStore.objects.values_list('response', 'expiration').get(hashkey=hide_hashkey)
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            exp_time = list(Captcha)[1].strftime('%Y-%m-%d %H:%M:%S')
            if now_time>exp_time:
                Result_Data = {}
                Result_Data["status"] = 201
                Result_Data["message"] = "验证码过期"
                return Response(Result_Data, status=status.HTTP_201_CREATED)
            captchaResponse = int(list(Captcha)[0])
        except CaptchaStore.DoesNotExist:
            Result_Data = {}
            Result_Data["status"] = 201
            Result_Data["message"] = "验证码错误"
            return Response(Result_Data, status=status.HTTP_201_CREATED)
        if captchaResponse == int(captcha):
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # from django.contrib.auth.tokens import default_token_generator
                    from CMS.auth.tokens import default_token_generator
                    #print (request.user)
                    # #
                    # # token = default_token_generator.make_token(user=request.user)
                    # #
                    # # return Response(default_token_generator.check_token(user=request.user,token=token))
                    token = default_token_generator.create_user_token(user)

                    # UserToken.objects.create()


                    # from django.contrib.auth import get_user_model
                    # UserModel = get_user_model()
                    # user = UserModel._default_manager.get_by_natural_key(user.name)
                    # print (user)
                    # from CMS.models import UserToken
                    # UserToken.objects.filter(user_id=user.pk).delete()
                    # UToken = UserToken()
                    # UToken.user_id     = user.pk
                    # UToken.key         = token
                    # UToken.created_at  = user.last_login
                    # delta = datetime.timedelta(days=settings.PASSWORD_RESET_TIMEOUT_DAYS)
                    # expire_date = user.last_login + delta
                    # UToken.expire_date = expire_date.strftime('%Y-%m-%d %H:%M:%S')
                    # UToken.save()

                    to_json_response={
                        'id':user.pk,#0,#str(list(id)[0]),
                        'user': str(request.user),
                        'token':token,#str(list(token)[0]),
                        # 'last_login':user.last_login,
                        'status':'200',
                    }
                    return Response(to_json_response)
                    #return Response("SADF")
            else:
                Result_Data = {}
                Result_Data["status"] = 201
                Result_Data["message"] = "用户名或密码错误"
                return Response(Result_Data,status=status.HTTP_201_CREATED)
        else:
            Result_Data = {}
            Result_Data["status"] = 201
            Result_Data["message"] = "验证码错误"
            return Response(Result_Data, status=status.HTTP_201_CREATED)
    else:
        Result_Data = {}
        Result_Data["status"] = 201
        Result_Data["message"] = "请填写验证码"
        return Response(Result_Data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def GetGenresVideo(request):
    if request.method == "GET":
        try:
            Genres_id =int(request.GET.get('Genres_id'))
            if Genres_id == 0:
                Video_Models = Video.objects.all().order_by('sorting')
            else:
                Video_Models = Video.objects.filter(Genres=Genres_id).all().order_by('sorting')
        except: #TypeError ValueError:
            return Response("error",status=status.HTTP_400_BAD_REQUEST)
        VideoVersion_Serializer = VideoSerializer(Video_Models,many=True)
        return Response(VideoVersion_Serializer.data)

@api_view(['GET'])
def GetGenresImage(request):
    if request.method == "GET":
        try:
            Genres_id = int(request.GET.get('Genres_id'))
            is_recommend = int(request.GET.get('is_recommend'))

            if Genres_id == 0:
                if is_recommend > 0:
                    Image_Models = Image.objects.filter(is_recommend=is_recommend).all().order_by('sorting')
                else:
                    Image_Models = Image.objects.all().order_by('sorting')
            else:
                Image_Models = Image.objects.filter(Genres=Genres_id).all().order_by('sorting')
        except: #TypeError ValueError:
            return Response("error",status=status.HTTP_400_BAD_REQUEST)

    ImageVersion_Serializer = ImageSerializer(Image_Models, many=True)
    return Response(ImageVersion_Serializer.data)

@api_view(['GET'])
def GetGenresGame(request):
    if request.method == "GET":
        try:
            if request.GET.has_key('is_recommend'):
                is_recommend = int(request.GET.get('is_recommend'))
                Game_Models = Game.objects.filter(is_recommend=is_recommend).all().order_by('sorting')

            elif request.GET.has_key('is_latest'):
                is_latest =  int(request.GET.get('is_latest'))
                Game_Models = Game.objects.filter(is_latest=is_latest).all().order_by('sorting')

            elif request.GET.has_key('is_hottest'):
                is_hottest =  int(request.GET.get('is_hottest'))
                Game_Models = Game.objects.filter(is_hottest=is_hottest).all().order_by('sorting')

            elif request.GET.has_key('Genres_id'):
                Genres_id = int(request.GET.get('Genres_id'))
                if Genres_id == 0:
                    Game_Models = Game.objects.all().order_by('sorting')
                else:
                    Game_Models = Game.objects.filter(Genres=Genres_id).all().order_by('sorting')
        except:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)

        GameVersion_Serializer = GameSerializer(Game_Models, many=True)
        return Response(GameVersion_Serializer.data)

    # if request.method == "GET":
    #     try:
    #         Genres_id    = int(request.GET.get('Genres_id'))
    #         is_recommend = int(request.GET.get('is_recommend'))
    #         is_latest    = int(request.GET.get('is_latest'))
    #         is_hottest   = int(request.GET.get('is_hottest'))
    #         if Genres_id == 0:
    #             if is_recommend > 0:
    #                 Game_Models = Game.objects.filter(is_recommend=is_recommend).all().order_by('sorting')
    #             else:
    #                 Game_Models = Game.objects.all().order_by('sorting')
    #             # if is_latest > 0:
    #             #     Game_Models = Game.objects.filter(is_latest=is_latest).all().order_by('sorting')
    #             # else:
    #             #     Game_Models = Game.objects.all().order_by('sorting')
    #             #
    #             # if is_hottest > 0:
    #             #     Game_Models = Game.objects.filter(is_hottest=is_hottest).all().order_by('sorting')
    #             # else:
    #             #     Game_Models = Game.objects.all().order_by('sorting')
    #         else:
    #             Game_Models = Game.objects.filter(Genres=Genres_id).all().order_by('sorting')
    #     except: #TypeError ValueError:
    #         return Response("error",status=status.HTTP_400_BAD_REQUEST)
    #
    # GameVersion_Serializer = GameSerializer(Game_Models, many=True)
    # return Response(GameVersion_Serializer.data)