# -*- coding: utf-8 -*-
from django.conf.urls import url,include
#from django.views import views
from rest_framework import routers
from V1 import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

# router = routers.DefaultRouter()
# router.register(r'AppUpdateMessage',views.AppUpdateMessageViewSet)

#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^applast/$', views.AppLastVersion),
    url(r'^firmwarelast/$', views.FirmWareLastVersion),
    #url(r'^appheart/$',views.AppHeart_list),
    url(r'^download/', views.download),
    url(r'^appheart/(?P<pk>([A-Fa-f0-9]{2}-){5}[A-Fa-f0-9]{2})/$',views.AppHeart_Detail),

    url(r'^imagefile/',views.get_image_file_list),

    url(r'^create_captcha/',views.create_captcha),

    url(r'^login/',views.user_login),

    url(r'^GetGenresVideo/',views.GetGenresVideo),

    url(r'^GetGenresImage/',views.GetGenresImage),

    url(r'^GetGenresGame/',views.GetGenresGame),



]
urlpatterns = format_suffix_patterns(urlpatterns)