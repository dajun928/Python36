#encoding=utf-8
import requests


response = requests.get("http://www.baidu.com/")

print(response.content)