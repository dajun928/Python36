#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : tmp.py
@time : 2019/06/29 17:36:03
@func : 
"""

from bs4 import BeautifulSoup

from PIL import Image
from io import BytesIO
import requests
url='https://weibo.com/p/1005053803673000/photos?from=page_100505&mod=TAB#place'
webdata = requests.get(url).text



print(webdata)