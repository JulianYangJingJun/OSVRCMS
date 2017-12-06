"""OSVRCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views
from statistics.views import line_chart_json
from statistics.views import testview
from django.contrib.auth.views import login
from CMS import views
admin.autodiscover()

urlpatterns = [

    url(r'^$', views.index,name='home'),
    url(r'^', include('CMS.urls')),





    # url(r'^', views.index),
    #url(r'^CMSAPI/', include('CMSAPI.urls')),
    url(r'^V1/',include('V1.urls')),
    url(r'^BhfVCvJzeSQm/', admin.site.urls),
    #url(r'^pages/', include('django.contrib.flatpages.urls')),
    #url(r'^(?P<url>.*/)$', views.flatpage),
    #url(r'^dashboard/', include('dash.urls')),
    #django-dash RSS contrib plugin URLs:
    #url(r'^dash/contrib/plugins/rss-feed/',include('dash.contrib.plugins.rss_feed.urls')),
    #django-dash public dashboards contrib app:
    #url(r'^', include('dash.contrib.apps.public_dashboard.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^index/line_chart_json/', admin.site.admin_view(line_chart_json),name='line_chart_json'),
    url(r'^index/t/',testview),
    url(r'^accounts/login/$', login),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    #url(r'^filer/',include('filer.urls')),
    #url(r'^CMSHEART/',include('statistics.urls')),
    #url(r"^ddsss/", include("chat.urls",namespace="chat")),
    #url("", include("django_socketio.urls")),

    #url("", include("CMSCHAT.urls")),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r"^so/", include("django_socketio.urls")),
    #url("", include("chat.urls")),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
