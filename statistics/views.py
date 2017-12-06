# -*- coding: utf-8 -*-
from random import randint

import sys
from django.core.serializers import json
from django.views.generic import TemplateView
from chartjs.views.lines  import BaseLineChartView
from statistics.models    import *
from django.db.models import Count,Q


def testview(request):
    from django.http import HttpResponse, JsonResponse
    obj = AppHeart.objects.values_list('LOGINTIME').distinct().order_by('LOGINTIME')
    obj2 = AppHeart.objects.values_list('LOGINTIME').order_by('LOGINTIME')
    # obj3 = AppHeart.objects.values_list('CREATED_AT', flat=True).filter(Q(ONFIRST=1)).order_by('LOGINTIME')
    arr = arr_str_arr(obj)
    online_list = arr_str_arr(obj2)
    import itertools
    it = itertools.groupby(online_list)
    count = len(online_list)
    ids = ''
    news_ids = []
    for i in range(0,count):
        for j in range(i+1,count):
            if online_list[i] != online_list[j]:
                news_ids.append(online_list[i])




    return HttpResponse(str(arr) + "<BR>" + str(news_ids))
    # install_list = time_str_arr(obj3)
    # online_arr = arr_sort(online_list, arr)
    # install_arr = arr_sort(install_list, arr)
    # install_arr = arr_sort(install_list, arr)



class LineChartJSONView(BaseLineChartView):
    def get_date_arr(self):
        date_obj  = AppHeart.objects.values_list('LOGINTIME').distinct().order_by('LOGINTIME')
        arr = arr_str_arr(date_obj)
        return arr

    def get_online_arr(self):
        online_obj  = AppHeart.objects.values_list('LOGINTIME').order_by('LOGINTIME')
        online_list = arr_str_arr(online_obj)
        online_arr  = arr_sort(online_list,self.get_date_arr())
        return online_arr

    def get_install_arr(self):
        install_obj  = AppHeart.objects.values_list('CREATED_AT', flat=True).filter(Q(ONFIRST=1)).order_by('LOGINTIME')
        install_list = time_str_arr(install_obj)
        install_arr  = arr_sort(install_list, self.get_date_arr())
        return install_arr

    def get_labels(self):
        return self.get_date_arr()

    def get_providers(self):
        return ["在线量","装机量"]

    def get_data(self):
        try:
            return [self.get_online_arr(), self.get_install_arr()]
        except Exception:
            return ['']

def arr_sort_aa(base_Data_Obj,base_Date_Obj):
    return base_Data_Obj


#arr去重、计算总量
def arr_sort(base_Data_Obj,base_Date_Obj):
    import itertools
    arr_count = ""
    i = 0
    it = itertools.groupby(base_Date_Obj)
    ids_count = len(base_Date_Obj)
    for k, g in it:
        i = i + 1
        a = str(base_Data_Obj.count(k))
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


line_chart = TemplateView.as_view(template_name='admin/installedbase.html')
line_chart_json = LineChartJSONView.as_view()