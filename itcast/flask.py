#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : flask.py
@time : 2019/05/26 21:21:36
@func : 
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()