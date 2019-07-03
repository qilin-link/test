#!/usr/bin/env python
#_*_ coding:utf-8 _*_
class Animal(object):
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print self.name + '吃'