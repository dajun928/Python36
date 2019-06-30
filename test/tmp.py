#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : tmp.py
@time : 2019/06/29 17:36:03
@func : 
"""
import cv2
import platform

print("OS : ", platform.system())
print("platform : ", platform.platform())
print("version : ", platform.version())
print("arch : ", platform.architecture())
print("machine : ",  platform.machine())
print("name : ", platform.uname())
print("python vision : ", platform.python_version())
print("OpenCV Version : ", cv2.__version__)
