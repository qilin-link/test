#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

def func():
    print 'slash is a good man.'

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

#创建按钮
button1 = tkinter.Button(win, text='按钮', command=func, width=10, height=10)
button1.pack()

button2 = tkinter.Button(win, text='按钮', command=win.quit)
button2.pack()

win.mainloop()









