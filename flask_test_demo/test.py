#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : test.py
@time : 2019/06/19 23:35:08
@func : 
"""
#导入Flask扩展
from flask import Flask,render_template

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由及视图函数
@app.route('/')
def hello_world():
    return 'Hello 666777 World!'
    # return render_template('index.html')

# 启动程序
if __name__ == '__main__':
    app.run(debug=True)