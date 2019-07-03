#!/usr/bin/env python
#_*_ coding:utf-8 _*_
class Card(object):
    def __init__(self,cardId,cardPasswd,cardMoney):
        self.cardId = cardId
        self.cardPasswd = cardPasswd
        self.cardMoney = cardMoney
        self.cardLock = False