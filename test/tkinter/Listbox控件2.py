#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

#绑定变量
lbv = tkinter.StringVar()
#与BROWSE相似，但是不支持鼠标移动选中位置
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
lb.pack()
for item in ['good','nice','handsome','vg','vn']:
    lb.insert(tkinter.END, item)

#打印当前列表中的选项
print lbv.get()
#设置选项
lbv.set(('1','2','3'))

#绑定事件
def myPrint(event):
    print lb.curselection()
    print lb.get(lb.curselection())
lb.bind('<Double-Button-1>', myPrint)



win.mainloop()