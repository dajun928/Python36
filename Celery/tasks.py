# -*- coding:utf-8 -*-
#待解决
# tasks.py
import time
from celery import Celery

# app = Celery('hello', broker='redis://localhost:6379')
app = Celery('hello', broker='redis://47.107.177.19:16379')


@app.task
def hello():
    for i in list(range(1,100)):
        print (i)
        print ('hello world')
        time.sleep(0.05)
        # print 'hello world2'
        # time.sleep(0.05)
        # print 'hello world3'

