#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物
'''
from cat import Cat
from mouse import Mouse
from person import Person

tom = Cat('Tom')
jerry = Mouse('Jerry')

tom.eat()
jerry.eat()

#定义一个人类，可以喂猫和老鼠吃东西

per = Person()
'''
per.feedCat(tom)
per.feedMouse(jerry)
'''
#tom和jerry都继承自动物
per.feedAnimal(tom)
per.feedAnimal(jerry)



