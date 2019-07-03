#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
人
类名：Person
属性：gun
行为：fire

枪
类名：Gun
属性：bulletBox
行为：shoot

弹夹
类名：BulletBox
属性：bulletBox
行为：

'''
from person import Person
from gun import Gun
from bulletbox import BulletBox

#弹夹
bulletBox = BulletBox(5)

#枪
gun = Gun(bulletBox)

#人
per = Person('Tom',24,173,65,gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

