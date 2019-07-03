#!/usr/bin/env python
#_*_ coding:utf-8 _*_

    
#say(6)

def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner

@outer
def say(age):
    print 'Pike is %d years old.' % age
    
say(-10)