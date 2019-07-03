#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import csv

def readCsv(path):
    infoList = []
    with open(path, 'r') as f:
        allFileInfo = csv.reader(f)
        #print allFileInfo
        for row in allFileInfo:
            #print unicode(row,encoding='utf8')
            infoList.append(row)
        return infoList


path = r'D:\script\test\读写csv文件\威海计划费用.csv'
uipath = unicode(path, 'utf8')
info = readCsv(uipath)

'''
inpath = r'D:\script\test\读写csv文件\威海计划费用.csv'
uipath = unicode(inpath, 'utf8')
fin = open(uipath)
'''





