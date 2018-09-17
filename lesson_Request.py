#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/11/011 20:57
# @Author  : lishuai
# @Site    : 
# @File    : lesson_Request.py
# @Software: PyCharm

import urllib.request
from urllib import request, parse

url = 'https://python.org'
wangpan_url = 'https://pan.baidu.com/disk/home?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0&traceid=#/all?path=%2F&vmode=list'
url_post = 'http://httpbin.org/post'

def use_Request(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))
def param_to_Request():
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org',
    }
    dict = {
        'name': 'Germey'
    }
    data = bytes(parse.urlencode(dict), encoding='utf8')
    req = request.Request(url=url_post, data=data, headers=headers, method='POST')
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))

use_Request(wangpan_url)
#param_to_Request()