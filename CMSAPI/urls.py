# -*- coding: utf-8 -*-
from django.conf.urls import url,include
#from django.views import views
from rest_framework import routers
from CMSAPI import views,topic_views
from CMSAPI.Login_reg_views import obtain_auth_token
from CMSAPI.topic_views import Game_Topic
from .views import *

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'marks/game', views.topicViewSet)
# router.register(r'marks/video', views.VideotopicViewSet)
# router.register(r'marks/app', views.ApptopicViewSet)
# router.register(r'game',views.GameViewSet),
# router.register(r'game_free',views.Game_freeViewSet),

urlpatterns = [
   url(r'^', include(router.urls)),
    #普通视图
    # 1.获取最新推荐
    url(r'^recommends/$', views.recommends),
    url(r'^recommends/(?P<sort_type>[A-Za-z0-9]+)/$', views.recommends),
    url(r'^recommends/(?P<sort_type>[A-Za-z0-9]+)/(?P<type>[A-Za-z0-9]+)/$', views.recommends),
    # 2.获取下载量最多的游戏(最火的游戏)
    url(r'^game_hottest/$', views.game_hottest),
    #3.评分最高的内容
    url(r'^highest_marks/$', views.highest_marks),
    url(r'^highest_marks/(?P<sort_type>[A-Za-z0-9]+)/$', views.highest_marks),
    url(r'^highest_marks/(?P<sort_type>[A-Za-z0-9]+)/(?P<type>[A-Za-z0-9]+)/$', views.highest_marks),
    #4、免费游戏
    url(r'^game_free/$', views.game_free),
    #5、广告
    url( r'^ads/$',views.ad_list),
    url( r'^ads/(?P<id>[0-9]+)/$',views.ad_detail),
    #6、最新内容
    url(r'^lastest/$', views.lastest),
    url(r'^lastest/(?P<sort_type>[A-Za-z0-9]+)/$', views.lastest),
    url(r'^lastest/(?P<sort_type>[A-Za-z0-9]+)/(?P<type>[A-Za-z0-9]+)/$', views.lastest),
    #7、详情
    #-------------------------------------------详情
    #url(r'^game/$',views.game),/detail_info/[id]/[type]/
    url(r'^detail_info/(?P<pk>[0-9]+)/game/$',views.game_detail),
    url(r'^detail_info/(?P<pk>[0-9]+)/video/',views.video_detail),
    url(r'^detail_info/(?P<pk>[0-9]+)/app/$',views.app_detail),

    #8.评论
    url(r'^marks/game/$', topic_views.Game_Topic),
    url(r'^marks/game/(?P<id>[0-9]+)/$', topic_views.Game_Topic_Detail),
    url(r'^marks/video/$', topic_views.Video_Topic),
    url(r'^marks/video/(?P<id>[0-9]+)/$', topic_views.Video_Topic_Detail),
    url(r'^marks/app/$', topic_views.App_Topic),
    url(r'^marks/app/(?P<id>[0-9]+)/$', topic_views.App_Topic_Detail),
    # 用户登录
    url(r'^account/$', obtain_auth_token),  # 登录 获取token

]
