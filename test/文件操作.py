#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import pickle

myList = (1,2,3,4,5,'slash is a good man')
path = r'D:\test\a.txt'
f = open(path,'wb')
pickle.dump(myList, f)
f.close()

#读取
fl = open(path, 'rb')
tempList = pickle.load(fl)
print tempList
fl.close()