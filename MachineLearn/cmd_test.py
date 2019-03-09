#!/usr/bin/env python
#-*- coding:utf-8 -*-
import subprocess

cmd = 'ls'
a = subprocess.getstatusoutput(cmd)

print(type(a))
print(a[1])

