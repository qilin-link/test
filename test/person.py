#!/usr/bin/env python
#_*_ coding:utf-8 _*_

class Person(object):
    
    def __init__(self,name,age,height,weight,gun):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gun = gun
        
    def fire(self):
        self.gun.shoot()
        
    def run(self):
        print ("run")
    def eat(self,food):
        print ("eat " + food)