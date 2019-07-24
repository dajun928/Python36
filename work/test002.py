#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : test002.py
@time : 2019/07/22 00:01:51
@func : 
"""

import requests

# url="https://www.meitulu.com/item/17827_12.html"
url="https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/17827/45.jpg"
rsp = requests.post(url,timeout=100)

print(rsp.text)
print(rsp.content)