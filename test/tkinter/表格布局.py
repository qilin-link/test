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
label4 = tkinter.Label(win,text='handsome',bg='pink')

#表格布局
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)



win.mainloop()