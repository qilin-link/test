#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

#<ButtonRelease-1>释放鼠标左键
#<ButtonRelease-3>释放鼠标右键
#<ButtonRelease-2>释放鼠标中键
label = tkinter.Label(win, text='slash is a good man.', bg='red')
label.pack()
def func(event):
    print event.x, event.y
label.bind('<ButtonRelease-1>', func)




win.mainloop()