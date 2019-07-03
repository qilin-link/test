#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from animal import Animal

class Cat(Animal):
    def __init__(self,name):
        super(Cat,self).__init__(name)
        
    #def eat(self):
    #    print self.name + '吃'