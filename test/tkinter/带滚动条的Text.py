#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
#win.geometry('400x400+500+200')

'''
文本控件，用于显示多行文本
'''
#创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=30, height=15)
#side放到窗体的哪一侧    fill填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

#关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str = "Before many more years he went away to a great rich school, followed by the prayers of a family, and by the valet and the groom. There he had a suite of rooms, and two horses, and a pair of dogs with pedigrees longer than his own; and there he learned to smoke a brand of choice cigarettes, and to play poker, and to take a proper interest in race-track doings. There also, just when he was ready to come away and to take a great college by storm, Robbie met with an exciting adventure.[12] This is a work of realism, and works of realism always go into detail as to such matters; and so it must be explained that Robbie fell desperately in love with a pretty girl who lived in the country near the school; and that Robbie was young and handsome and wealthy and witty, and by no means disposed to put up with not having his own way; and that he had it; and that when he came to leave school, the girl fled from home and followed him; and that there were some blissful months in the city, and then some complications; and that when the crisis came Robbie was just on the point of getting married when the curiosity of his father was excited by his heavy financial demands; and, finally, that Mr. Chauncey van Rensselaer and Mr. Robert van Rensselaer held an interview in the former's study."
text.insert(tkinter.INSERT, str)





win.mainloop()