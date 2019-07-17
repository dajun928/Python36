#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : api_client.py
@time : 2019/07/17 22:51:56
@func : 
"""
import requests

# url="http://127.0.0.1:5001/"        # local test
url="http://47.107.177.19:8060/"    # remote test

responses=requests.get(url)
print(responses)
# 查看响应内容，response.text 返回的是Unicode格式的数据
print(responses.text)
