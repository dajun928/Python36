#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:homework
@file:printDate.py
@time:2019/02/04 17:14:10
"""

import calendar

def get_week_day(i):
  week_day_dict = {
    0 : u'星期一',
    1 : u'星期二',
    2 : u'星期三',
    3 : u'星期四',
    4 : u'星期五',
    5 : u'星期六',
    6 : u'星期天',
  }
  return week_day_dict[i]

def main():
    import datetime
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    # month=5
    rets=calendar.monthcalendar(year,month)
    for ret in rets:
        for index,i in enumerate(ret):
            if i!=0:
                # print("* * *")
                # print("##### " + str(year) + "年" + str(month) + "月" + str(i) + "日" + "  " + get_week_day(index))
                # print("1. ")

                print("-" * 62 + ">")
                print(str(year) + "年" + str(month) + "月" + str(i) + "日" + "  " + get_week_day(index))
                print("1. ")

if __name__ == '__main__':
    main()






