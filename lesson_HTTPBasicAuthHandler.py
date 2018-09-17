#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17/017 20:20
# @Author  : lishuai
# @Site    : 
# @File    : lesson_HTTPBasicAuthHandler.py
# @Software: PyCharm

from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener
from urllib.error import URLError

username = 'lwx430932'
password = 'ss518528'
url = 'https://github.com/lwx430932/crawler_learning'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
