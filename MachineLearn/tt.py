# coding: utf-8

import sys
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
