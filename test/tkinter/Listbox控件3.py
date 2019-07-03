#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
#win.geometry('400x400+500+200')

#EXTENDED可以使listbox支持shift和control
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED)
lb.pack()
for item in ['good','nice','handsome','vg','vn','good1','nice1','handsome1','vg1','vn1',
             'good3','nice3','handsome3','vg3','vn3']:
    lb.insert(tkinter.END, item)

#按住shift，可以实现连选
#按住control，可以实现多选
#滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
#额外给属性赋值
sc['command'] = lb.yview















win.mainloop()