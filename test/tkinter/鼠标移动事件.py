#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')


#<B1-Motion>左键移动
#<B3-Motion>右键移动
#<B2-Motion>中键移动
label = tkinter.Label(win, text='slash is a good man.')
label.pack()
def func(event):
    print event.x, event.y
label.bind('<B1-Motion>', func)







win.mainloop()