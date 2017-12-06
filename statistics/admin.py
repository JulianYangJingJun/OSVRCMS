# -*- coding: utf-8 -*-
#!E:\www\python\OSVRCMS\env python
# @Date    : Date
# @Author  : Julian Yang (aqkt_436@163.com)
# @Link    : http://www.abbstyle.com

from django.contrib import admin
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.conf.urls import  url,include
from statistics.models import *
from statistics.forms import *
from django.contrib.admin.sites import AdminSite

# Register your models here.

class AppHeartAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        return super(AppHeartAdmin, self).__init__(*args, **kwargs)

    def get_urls(self):
        from views import LineChartJSONView,line_chart,line_chart_json
        urls = super(AppHeartAdmin, self).get_urls()
        my_urls = [url(r'^installedbase/$', self.admin_site.admin_view(line_chart))]
        return my_urls + urls


    list_display = ('id','APPIP','MACADDRESS','LOGINTIME','HEARTRATE','online')
    search_fields = ('APPIP',)
    list_filter = ('MACADDRESS','LOGINTIME', )
    #actions = ['some_other_action']
    #models =AppHeart
    form = AppHeartForm
    #
    # def my_view(self,request):
    #     context = {'admin_site': '111','title': "323232",}
    #     template = 'admin/TT.html'
    #     return render_to_response(template, context)
    #
    #
    # def get_urls(self):
    #     urls = super(AppHeartAdmin, self).get_urls()
    #     my_urls = [url(r'^my_view/$', self.admin_site.admin_view(self.my_view, cacheable=True))]
    #     return my_urls + urls
    #
    # def admin_my_view(request, model_admin):
    #     opts = model_admin.model.Meta
    #     admin_site = model_admin.admin_site
    #     has_perm = request.user.has_perm(opts.app_label + '.' + opts.get_change_permission())
    #     context = {'admin_site': admin_site.name,
    #                'title': "My Custom View",
    #                'opts': opts,
    #                'root_path': '/%s' % admin_site.root_path,
    #                'app_label': opts.app_label,
    #                'has_change_permission': has_perm}
    #     template = 'admin/TT.html'
    #     return render_to_response(template, context)

# class AppHeartAdmin_ZJL(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super(AppHeartAdmin_ZJL,self).get_urls()
#         my_urls = patterns('',(r'^my_view/$', self.my_view))
#         return my_urls + urls
#     def my_view(self,request):
#         print (12)
#         pass


    # #然后把对应的js或css文件写入到static下边的指定文件里吧，运行admin的页面会额外引用你自己的css和js文件
    # class Media:
    #     js = ('js/my_own_admin.js',)
    #     css = {
    #         'all': ('css/admin/my_own_admin.css',)
    #     }


admin.site.register(AppHeart,AppHeartAdmin)
