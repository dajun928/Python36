#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 
@file : log_to_local.py
@time : 2019/03/16 18:43:26
@func : windows上监控日志增量信息并插入数据库
"""
import time
import re

start_point=0
log_path=r"D:\test\a.txt"
pattern=r"[ ]"

while True:
    with open(log_path,"rb") as fo:
        fo.seek(start_point,1)
        lines=fo.readlines()
        for line in lines:
            text=line.decode().replace('\r\n','')
            if text:
                result=re.split(pattern,text,2)
                print(result)
        start_point=fo.tell()
        print(start_point)
    time.sleep(10)



