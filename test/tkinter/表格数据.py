#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter
from tkinter import ttk
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('600x400+500+200')

#表格
tree = ttk.Treeview(win)
tree.pack()

#定义列
tree['columns']=('姓名','年龄','身高','体重')
#设置列，列还不显示
tree.column('姓名', width=100)
tree.column('年龄', width=100)
tree.column('身高', width=100)
tree.column('体重', width=100)

#设置表头
tree.heading('姓名', text='姓名-name')
tree.heading('年龄', text='年龄-age')
tree.heading('身高', text='身高-height')
tree.heading('体重', text='体重-weight')

#添加数据
tree.insert('',0,text='line1',values=('张驰','38','172','79'))
tree.insert('',1,text='line2',values=('陈旭','29','175','83'))
tree.insert('',2,text='line3',values=('李菲','21','163','51'))









win.mainloop()