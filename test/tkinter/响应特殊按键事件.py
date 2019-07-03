#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

label = tkinter.Label(win, text='slash is a good man.', bg='red')
#设置焦点
label.focus_set()
label.pack()

#<Shift_L>左shift
#<Shift_R>
#<F5>
#<Return>回车
#<BackSpace>退格
def func(event):
    print 'event.char = ', event.char
    print 'event.keycode = ', event.keycode
label.bind('<Shift_L>', func)




win.mainloop()