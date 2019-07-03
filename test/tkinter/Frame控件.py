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
框架控件
在屏幕上显示一个矩形区域，多作为容器控件
'''
frm = tkinter.Frame(win)
frm.pack()


#left
frm_1 = tkinter.Frame(frm)
tkinter.Label(frm_1, text='左上', bg='pink').pack(side=tkinter.TOP)
tkinter.Label(frm_1, text='左下', bg='blue').pack(side=tkinter.TOP)
frm_1.pack(side=tkinter.LEFT)

#right
frm_2 = tkinter.Frame(frm)
tkinter.Label(frm_2, text='右上', bg='green').pack(side=tkinter.TOP)
tkinter.Label(frm_2, text='右下', bg='yellow').pack(side=tkinter.TOP)
frm_2.pack(side=tkinter.RIGHT)









win.mainloop()