#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 
@file : hello.py
@time : 2019/03/09 01:04:39
@func : 
"""
import platform

# 获取操作系统详细信息

print(platform.platform())      #获取操作系统名称及版本号，'Windows-7-6.1.7601-SP1'
print(platform.version())       #获取操作系统版本号，'6.1.7601'
print(platform.architecture())  #获取操作系统的位数，('32bit', 'WindowsPE')
print(platform.machine())       #计算机类型，'x86'
print(platform.node())          #计算机的网络名称，'hongjie-PC'
print(platform.processor())     #计算机处理器信息，'x86 Family 16 Model 6 Stepping 3, AuthenticAMD'
print(platform.uname())         #包


#   python的一些信息
print(platform.python_version())
