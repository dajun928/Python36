#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : api_server.py
@time : 2019/07/17 22:51:30
@func : 
"""

#导入Flask扩展
from flask import Flask

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由及视图函数
@app.route('/')
def hello_world():
    return 'Hello! This is running in docker'

# 启动程序
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)