#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

'''
输入控件
用于显示简单的文本内容
'''
#绑定变量
e = tkinter.Variable()
#show 密文显示
#entry = tkinter.Entry(win,show='*')
entry = tkinter.Entry(win,textvariable=e)
entry.pack()
#e就代表输入框这个对象
#设置值
e.set('slash7 is a good man.')
#取值
print e.get()
print entry.get()


win.mainloop()