#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

#<Key>响应所有的按键
label = tkinter.Label(win, text='slash is a good man.', bg='red')
#设置焦点
label.focus_set()
label.pack()

def func(event):
    print 'event.char = ', event.char
    print 'event.keycode = ', event.keycode
label.bind('<Key>', func)

'''
#给小控件添加，需要设置焦点；给win添加，不需要设置焦点
def func(event):
    print 'event.char = ', event.char
    print 'event.keycode = ', event.keycode
win.bind('<Key>', func)
'''

win.mainloop()