#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : hello.py
@time : 2020/06/08 23:20:36
@func : 
"""
# -*- coding: utf-8 -*-

class Person(object):
    """Silly Person"""
    def __new__(cls, *args, **kwargs):
        print('__new__ called.')
        # return super(Person, cls).__new__(cls)
        return object.__new__(cls)

    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age

    def __str__(self):
        return '<-----Person=====: %s(%s)>' % (self.name, self.age)

if __name__ == '__main__':
    piglei = Person('piglei', 24)
    print(piglei)
