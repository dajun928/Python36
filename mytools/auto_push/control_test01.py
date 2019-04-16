#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : control.py
@time : 2019/04/16 00:09:31
@func : 
"""

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import subprocess

#本类的方法
def my_job01():
    print('Tick! The time is: %s' % datetime.now())
    cmd = 'sh push_test02.sh control.py'
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # 设置定时调度本类的方法
    scheduler.add_job(my_job01, 'cron', hour ='16',minute ='20')

    # 启动调度
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()






