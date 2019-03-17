#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 3.6.3
@file : auto_shutdown.py
@time : 2019/03/16 16:16:23
@func : 连接本地windows 并执行关机命令
"""

import os
import time
# reload(sys)
# sys.setdefaultencoding("GBK")
# shutdown computer after time_diff seconds
def shutdown(seconds):
    print (str(seconds) + u' 秒钟后将会关机...')
    time.sleep(seconds)
    print (u'关机啦。。。')
    os.system('shutdown -s -f -t 1')

def main():
    hour = input(u'延迟关机秒钟数：')
    print (hour)
    shutdown(int(hour))

if __name__ == '__main__':
    main()
