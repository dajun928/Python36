#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 3.6.3
@file : win_control.py
@time : 2019/03/16 16:16:23
@func : 连接本地windows或者linux 并执行操作命令
"""
import subprocess

cmd = 'ls'
a = subprocess.getstatusoutput(cmd)

print(type(a))
print(a[0])
print(a[1])


