#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : https://blog.csdn.net/qq_37616069/article/details/80376776
@file : test_demo.py
@time : 2019/06/27 23:36:35
@func :


使用response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，大多数 Unicode 字符集都能被无缝地解码。

使用response.content 时，返回的是服务器响应数据的原始二进制字节流，可以用来保存图片等二进制文件。
"""
import requests

url="http://127.0.0.1:5000/"
responses=requests.get(url)

print(responses)

# 查看响应内容，response.text 返回的是Unicode格式的数据
print(responses.text)

# 查看响应内容，response.content返回的字节流数据
print(responses.content)

# 查看完整url地址
print(responses.url)

# 查看响应头部字符编码
print(responses.encoding)

# 查看响应码
print(responses.status_code)
print(responses.json())
