#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : https://www.jianshu.com/p/1d525c86515d
           https://blog.csdn.net/eastmount/article/details/50256163
@file : tmp.py
@time : 2019/06/29 17:36:03
@func : 结巴中文分词介绍
"""
import jieba

# 全模式
text = "我来到北京清华大学"
seg_list = jieba.cut(text, cut_all=True)
print(u"[全模式]: ", "/ ".join(seg_list))

# 精确模式
seg_list = jieba.cut(text, cut_all=False)
print(u"[精确模式]: ", "/ ".join(seg_list))

# 默认是精确模式
seg_list = jieba.cut(text)
print(u"[默认模式]: ", "/ ".join(seg_list))

# 搜索引擎模式
seg_list = jieba.cut_for_search(text)
print(u"[搜索引擎模式]: ", "/ ".join(seg_list))

