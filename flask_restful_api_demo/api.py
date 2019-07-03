#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : api.py
@time : 2019/06/27 21:47:02
@func : https://blog.csdn.net/chenmozhe22/article/details/82347813
"""
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()

