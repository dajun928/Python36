# -*- coding:utf-8 -*-
#待解决
# tasks.py
import time
from celery import Celery

# app = Celery('hello', broker='redis://localhost:6379')


app = Celery('TASK',broker='redis://47.107.177.19',backend='redis://47.107.177.19')


@app.task
def add(x, y):
    print("running...", x, y)
    return x + y