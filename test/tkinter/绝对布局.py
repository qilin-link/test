#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter
from cProfile import label

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

label1 = tkinter.Label(win,text='good',bg='blue')
label2 = tkinter.Label(win,text='nice',bg='yellow')
label3 = tkinter.Label(win,text='cool',bg='red')

#绝对布局，窗口的变化对位置没有影响
label1.place(x=10,y=10)
label2.place(x=50,y=50)
label3.place(x=100,y=100)










win.mainloop()