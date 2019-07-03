#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter
from tkinter import ttk

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')


tree = ttk.Treeview(win)
tree.pack()

#添加一级树枝
treeF1 = tree.insert('',0,'中国',text='中国CHN',values=('F1'))
treeF2 = tree.insert('',1,'美国',text='美国USA',values=('F2'))
treeF3 = tree.insert('',2,'英国',text='英国ENG',values=('F3'))

#二级树枝
treeF1_1 = tree.insert(treeF1,0,'黑龙江',text='黑龙江',values=('F1_1'))
treeF1_2 = tree.insert(treeF1,1,'吉林',text='吉林',values=('F1_2'))
treeF1_3 = tree.insert(treeF1,2,'辽宁',text='辽宁',values=('F1_3'))

treeF2_1 = tree.insert(treeF2,0,'纽约',text='纽约',values=('F2_1'))
treeF2_2 = tree.insert(treeF2,1,'新泽西',text='新泽西',values=('F2_2'))
treeF2_3 = tree.insert(treeF2,2,'休斯顿',text='休斯顿',values=('F2_3'))

treeF3_1 = tree.insert(treeF3,0,'曼彻斯特',text='曼彻斯特',values=('F3_1'))
treeF3_2 = tree.insert(treeF3,1,'埃佛顿',text='埃佛顿',values=('F3_2'))
treeF3_3 = tree.insert(treeF3,2,'利物浦',text='利物浦',values=('F3_3'))

#三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,'哈尔滨',text='哈尔滨',values=('F1_1_1'))
treeF1_1_2 = tree.insert(treeF1_1,1,'牡丹江',text='牡丹江',values=('F1_1_2'))
treeF1_1_3 = tree.insert(treeF1_1,2,'漠河',text='漠河',values=('F1_1_3'))




win.mainloop()