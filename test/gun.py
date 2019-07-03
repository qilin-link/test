#!/usr/bin/env python
#_*_ coding:utf-8 _*_
class Gun(object):
    def __init__(self,bulletBox):
        self.bulletBox = bulletBox
        
    def shoot(self):
        if self.bulletBox.bulleCount == 0:
            print "没有子弹了"
        else:
            self.bulletBox.bulleCount -= 1
            print "剩余子弹：%d颗" % self.bulletBox.bulleCount
        