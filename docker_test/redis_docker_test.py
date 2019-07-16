#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : redis_docker_test.py
@time : 2019/07/16 22:05:17
@func : 
"""
import redis
# 连接Linux服务器上的redis

re = redis.Redis(host='47.107.177.19', port=16379)
# re.set('key_name', 'value_tom')
# re.set('key_name02', 'value_tom2')
# re.set('key_name03', 'value_tom3')

# print(re.get('key_name'))
# print(re.get('key_name02'))
# print(re.get('key_name03'))
# print(re.get('abc'))
# print(re.get('12'))
print(re.get('666'))