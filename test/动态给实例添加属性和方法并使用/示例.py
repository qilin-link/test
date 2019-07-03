#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#创建一个空类
from types import MethodType
class Person(object):
    __slots__ = ('name','age','speak')

per = Person()
#动态添加属性，这体现了动态语言的特点（灵活）
per.name = 'lilei'
print per.name
#动态添加方法
def say(self):
    print 'my name is ' + self.name
'''
per.speak = say
per.speak(per)
'''
per.speak = MethodType(say,per) 
per.speak()   
    
#思考：如果我们想要限制实例的属性怎么办？
#比如，只允许给对象添加name,age,height,weight属性

#解决：定义类的时候，定义一个特殊的属性（__slots__），可以限制动态添加的属性
    
per.height = 180
print per.height    
    
    
    
    
    
    
    
    