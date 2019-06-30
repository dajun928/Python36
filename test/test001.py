#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : test001.py
@time : 2019/06/30 22:26:32
@func : 
"""
# built in python 3.5.2
# 作者：陈常鸿
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

path = r'D:\test'
num = 1
content = 'http://www.youzi4.cc/mm/'  #
# 爬取具体图片连接
while True:
    html = '.html'
    max = 100
    print(num)
    for n in range(1, max):
        url = content + str(num) + '/' + str(num) + '_' + str(n) + html  # mm/x/x_num.html
        webdata = requests.get(url).text
        soup = BeautifulSoup(webdata, 'lxml')
        try:
            link = soup.select("img.IMG_show")
            jpg = link[0].get('src')  # 定位后是一个列表，尽管只有列表只有一个，他还是一个列表，所以需要定位到[0]
            pic = requests.get(jpg)
            image = Image.open(BytesIO(pic.content))
            image.save(path + str(num) + '_' + str(n) + '.jpg')
            print("完成：", n)
        except IndexError:
            break
        except OSError:
            continue

    print('下载完成！')
    num += 1
