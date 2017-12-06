#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: Julian
@license: Apache Licence 
@contact: aqkt_436@163.com
@site: http://www.abbstyle.com
@software: PyCharm
@time: 2017/6/13 10:12
"""
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import json
import sys
class FileStorage(FileSystemStorage):
    from django.conf import settings
    filetype=None
    def __init__(self,location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        #初始化
        super(FileStorage,self).__init__(location,base_url)

    #重写_save方法
    def _save(self, name, content):
        import os, time, random
        # 文件扩展名
        ext = os.path.splitext(name)[1]
        # 文件目录
        d = os.path.dirname(name)+'./app/upload/'+self.filetype+'/'+time.strftime('%Y%m%d')
        # 定义文件名，年月日时分秒随机数
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 100)
        # 重写合成文件名
        name = os.path.join(d, fn + ext)
        # 调用父类方法
        return super(FileStorage, self)._save(name, content)