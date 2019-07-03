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
数值范围控件
'''

def updata():
    print v.get()

#绑定一个变量
v = tkinter.StringVar()

#increment    步长    默认为1
#values    最好不要与from_=0, to=100, increment=2同时使用 values=(0,2,4,6,8)
#command    只要值改变就会执行对应的方法
#sp = tkinter.Spinbox(win, values=(0,2,4,6,8))
sp = tkinter.Spinbox(win, from_=0, to=100, increment=1, textvariable=v,
                     command=updata)
sp.pack()

#设置值
v.set(20)
#取值
print v.get()













win.mainloop()