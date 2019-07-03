#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

#菜单条
menubar = tkinter.Menu(win)

menu = tkinter.Menu(menubar, tearoff=False)
for item in ['Python','C','C#','OC','C++',"JS",'退出']:
    menu.add_command(label=item)

menubar.add_cascade(label='语言', menu=menu)

def showMenu(event):
    menubar.post(event.x_root, event.y_root)

win.bind('<Button-3>', showMenu)


win.mainloop()