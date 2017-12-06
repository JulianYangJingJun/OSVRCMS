#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: Julian
@license: Apache Licence 
@contact: aqkt_436@163.com
@site: http://www.abbstyle.com
@software: PyCharm
@file: FileMd5.py
@time: 2017/6/13 13:34
"""
import hashlib
import os
class FileMd5(object):
    #初始化函数
    def __init__(self,word,fname):
        self.word = word
        self.fname= fname

    def md5hex(self):
        """ MD5加密算法，返回32位小写16进制符号 """
        if isinstance(self.word, unicode):
            word = self.word.encode("utf-8")
        elif not isinstance(self.word, str):
            word = str(self.word)
        m = hashlib.md5()
        m.update(self.word)
        return m.hexdigest()

    def md5sum(self):
        """ 计算文件的MD5值 """
        def read_chunks(fh):
            fh.seek(0)
            chunk = fh.read(8096)
            while chunk:
                yield chunk
                chunk = fh.read(8096)
            else:  # 最后将游标放回文件开头
                fh.seek(0)

        m = hashlib.md5()
        if isinstance(self.fname, basestring) and os.path.exists(self.fname):
            with open(self.fname, "rb") as fh:
                for chunk in read_chunks(fh):
                    m.update(chunk)
        # 上传的文件缓存 或 已打开的文件流
        elif self.fname.__class__.__name__ in ["StringIO", "StringO"] or isinstance(self.fname, file):
            for chunk in read_chunks(self.fname):
                m.update(chunk)
        else:
            return ""
        return m.hexdigest()