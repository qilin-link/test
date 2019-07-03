#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
概念：是一个闭包，把一个函数当做参数，返回一个替代版的函数，本质上就是一个返回函数的函数
'''

#简单的装饰器
def func1():
    print 'Pike is a good man.'

def outer(func):
    def inner():
        print '*************'
        func()
    return inner

f = outer(func1)
f()











