#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : flask_test.py
@time : 2019/06/16 23:10:59
@func : 
"""
#导入Flask扩展
from flask import Flask

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由及视图函数
@app.route('/')
def hello_world():
    return 'Hello World!'

# 启动程序
if __name__ == '__main__':
    app.run()