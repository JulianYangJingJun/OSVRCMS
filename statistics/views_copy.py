# -*- coding: utf-8 -*-
from random import randint

import sys
from django.core.serializers import json
from django.views.generic import TemplateView
from chartjs.views.lines  import BaseLineChartView
from statistics.models    import *
from django.db.models import Count,Q




class LineChartJSONView(BaseLineChartView):
    obj  = AppHeart.objects.values_list('LOGINTIME').distinct().order_by('LOGINTIME')
    obj2 = AppHeart.objects.values_list('LOGINTIME').order_by('LOGINTIME')
    obj3 = AppHeart.objects.values_list('CREATED_AT',flat=True).filter(Q(ONFIRST=1)).order_by('LOGINTIME')
    print (obj3)
    def get_labels(self):
        arr = arr_str_arr(self.obj)
        return arr
    def get_providers(self):
        return ["在线量","装机量"]
    def get_data(self):
        try:
            online_list  = arr_str_arr(self.obj2)
            install_list = time_str_arr(self.obj3)
            online_arr   = arr_sort(online_list, self.get_labels())
            install_arr = arr_sort(install_list, self.get_labels())
            return [online_arr, install_arr]
        except Exception:
            return ['']

#arr去重、倒排序、计算总量
def arr_sort(baseDataObj,baseDateTimeObj):
    import itertools
    arr_count = ""
    i = 0
    it = itertools.groupby(baseDateTimeObj)
    ids_count = len(baseDateTimeObj)
    for k, g in it:
        i = i + 1
        a = str(baseDataObj.count(k))
        if i < ids_count:
            arr_count = arr_count + a + ","
        else:
            arr_count = arr_count + a
    arr_count = arr_count.split(',')
    return arr_count

#arr转str转arr
def arr_str_arr(object,count=None):
    o = list(object)
    result = ""
    i = 0
    for oo in o:
        i = i + 1
        a = len(o)
        if i < a:
            result = result + (' '.join(oo).encode("utf-8")+ ",")
        else:
            result = result + (' '.join(oo).encode("utf-8"))
    arr = result.split(',')
    return arr

#time转str转arr
def time_str_arr(object,count=None):
    i = 0
    arr_sum = len(object)
    arr_time = ""
    for oo in object:
        i = i + 1
        if i < arr_sum:
            arr_time = arr_time + oo.strftime("%Y-%m-%d") + ","
        else:
            arr_time = arr_time + oo.strftime("%Y-%m-%d")
    arr_time = arr_time.split(',')
    return arr_time

# 去重排序 算出count
# def arr_sort(object):
#     import itertools
#     arr_count = ""
#     i = 0
#     it = itertools.groupby(object)
#     ids_count = len(object)
#     for k, g in it:
#         i = i + 1
#         a = str(object.count(k))
#         if i < ids_count:
#             arr_count = arr_count + a + ","
#         else:
#             arr_count = arr_count + a
#     arr_count = arr_count.split(',')
#     return arr_count




line_chart = TemplateView.as_view(template_name='admin/installedbase.html')
line_chart_json = LineChartJSONView.as_view()