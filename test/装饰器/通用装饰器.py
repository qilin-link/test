#!/usr/bin/env python
#_*_ coding:utf-8 _*_


def outer(func):
    def inner(*args,**kwargs):
        #添加修饰的功能
        print '*****************'
        func(*args,**kwargs)
    return inner

@outer
def say(name,age):
    print 'My name is %s, and I am %d years old.' % (name,age)
    
say('Pike',6)



