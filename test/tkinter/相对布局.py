#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')


label1 = tkinter.Label(win,text='good',bg='blue')
label2 = tkinter.Label(win,text='nice',bg='yellow')
label3 = tkinter.Label(win,text='cool',bg='red')

#相对布局，窗体改变对控件有影响
#tkinter.BOTH
label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.pack()





win.mainloop()