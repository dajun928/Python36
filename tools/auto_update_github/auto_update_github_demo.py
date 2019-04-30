#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 3.6.3
@file : auto_update_github.py
@time : 2019/04/30 21:09:26
@func : 
"""

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import subprocess
import os
import shutil

def copydir(path, out):
    for files in os.listdir(path):
        name = os.path.join(path, files)
        back_name = os.path.join(out, files)
        if os.path.isfile(name):
            if os.path.isfile(back_name):
                # print(back_name)
                pass
            else:
                # print(back_name)
                pass
        else:
            if not os.path.isdir(back_name):
                os.makedirs(back_name)
                copydir(name, back_name)

def copyfile(src, dsc):
    tmp_list=[]
    for root, dirs, files in os.walk(src):
        if dirs:
            dsc_path=dsc
        else:
            dsc_path=os.path.join(dsc, os.path.split(root)[1])
        for file in files:
            src_file=os.path.join(root,file)
            tmp_trup=(src_file,dsc_path)
            tmp_list.append(tmp_trup)
    return tmp_list

def cut_single_file():
    A = r"/root/homework"
    B = r"/root/Projects/gitdemo/test/Tool/Tool"

    # A=r"D:\test\a"
    # B=r"D:\test\b"
    copydir(A, B)
    result = copyfile(A, B)
    if result:
        src_file, dsc_path = result.pop()
        print(src_file)
        shutil.move(src_file, dsc_path)

#本类的方法
def push():
    print('Tick! The time is: %s' % datetime.now())
    cmd = 'sh push.sh auto_control.py'
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # 设置定时调度本类的方法
    scheduler.add_job(cut_single_file, 'cron', hour ='23',minute ='22')

    scheduler.add_job(push, 'cron', hour ='23',minute ='23')

    # 启动调度
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
    # cut_single_file()