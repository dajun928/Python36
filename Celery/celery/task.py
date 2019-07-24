# -*- coding:utf-8 -*-

from celery import Celery
app = Celery('demo', broker='redis://127.0.0.1/1', backend='redis://127.0.0.1/2')  # 使用redis作为broker和接受返回值

@app.task
def test_task():
    print('testing')



















