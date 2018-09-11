#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10/010 21:43
# @Author  : lishuai
# @Site    : 
# @File    : lesson_urlopen.py
# @Software: PyCharm
'''
a new urllib package was created. It consists of code from
urllib, urllib2, urlparse, and robotparser. The old
modules have all been removed. The new package has five submodules:
urllib.parse, urllib.request, urllib.response,
urllib.error, and urllib.robotparser. The
urllib.request.urlopen() function uses the url opener from
urllib2. (Note that the unittests have not been renamed for the
beta, but they will be renamed in the future.)
'''
import urllib.request
import urllib.parse
import socket
import urllib.error

url = "http://www.baidu.com"
url_post = "http://httpbin.org/post"
url_get = "http://httpbin.org/get"

def use_urlopen():
    response = urllib.request.urlopen(url)
    #print(response.read().decode('utf-8'))
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Server'))
def data_for_urlopen():
    data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
    response = urllib.request.urlopen(url_post, data=data)
    print(response.read())
def timeout_for_urlopen():
    try:
        urllib.request.urlopen(url_get, timeout=0.1)
    except Exception as e:
        if isinstance(e, socket.timeout):
            print("TIME OUT ERROR")

timeout_for_urlopen()