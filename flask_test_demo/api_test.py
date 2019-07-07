#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : api_test.py
@time : 2019/07/07 13:36:45
@func : 
"""
import requests

# url="http://127.0.0.1:5000/"
# url="http://172.18.127.255:8088/"
url="http://47.107.177.19:8088/"
responses=requests.get(url)
print(responses)
# 查看响应内容，response.text 返回的是Unicode格式的数据
print(responses.text)
print(responses.content)