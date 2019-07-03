#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')


#<Enter>鼠标光标进入控件时触发
#<Leave>鼠标光标离开控件时触发
label = tkinter.Label(win, text='slash is a good man.', bg='red')
label.pack()
def func(event):
    print event.x, event.y
label.bind('<Enter>', func)







win.mainloop()