#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#需求：当程序遇到问题时不让程序结束，而越过错误向下执行
'''
try except else
格式：
try:
    语句t
except 错误码  as e:
    语句1
    except 错误码  as e:
    语句2
......
except 错误码  as e:
    语句n
else:
    语句e
 
注意：else语句可有可无

作用：用来检测try语句块中的错误，从而让except语句捕获错误信息并处理

逻辑：当程序执行到try-except-else语句时    
1、如果当try“语句t”执行出现错误，会匹配第一个错误码。如果匹配上就执行对应“语句”。
2、如果当try“语句t”执行出现错误，没有匹配的异常，错误将会被提交到上一层的try语句，或者到程序的最上层。
3、如果当try“语句t”执行没有出现错误，执行else下的“语句e”（你得有）

'''

try:
    print 3/1
except ZeroDivisionError as e:
    print '除数为0了'
else:
    print '代码没有问题'
    
print '************'

#使用except而不使用任何的错误类型
try:
    print 4/0
except:
    print '程序出现了异常'

#使用except带着多种异常
try:
    print 5/0
except (NameError,ZeroDivisionError):
    print '出现了NameError或ZeroDivisionError' 





















