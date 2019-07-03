#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')


def func(event):
    print 'event.char = ', event.char
    print 'event.keycode = ', event.keycode
win.bind('a', func)



win.mainloop()