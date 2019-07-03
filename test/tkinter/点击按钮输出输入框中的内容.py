#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

def showInfo():
    print entry.get()

entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win, text='打印', command=showInfo)
button.pack()






win.mainloop()