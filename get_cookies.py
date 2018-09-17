#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17/017 21:00
# @Author  : lishuai
# @Site    : 
# @File    : get_cookies.py
# @Software: PyCharm

import http.cookiejar, urllib.request

url = "http://www.baidu.com"
filename = 'cookies.txt'
def get_cookies(url, filename):

    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)

def use_cookies(url, filename):
    cookie = http.cookiejar.MozillaCookieJar()
    cookie.load(filename, ignore_expires=True, ignore_discard=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    print(response.read().decode('utf-8'))

get_cookies(url, filename)
use_cookies(url, filename)