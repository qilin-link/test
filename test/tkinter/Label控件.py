#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter

win = tkinter.Tk()
win.title('Test')
win.geometry('400x400+500+200')

'''
Label: 标签控件，可以显示文本
'''
#win:父窗体
#text:显示的文本内容
#bg:背景色
#fg:字体颜色
#wraplength:指定text文本中多宽进行换行
#justify:设置换行后的对齐方式
#anchor:位置 n e s w 东南西北，center居中
label = tkinter.Label(win,
                      text='slash',
                      bg='blue',
                      fg='white',
                      font=('黑体',20),
                      width=10,
                      height=4,
                      wraplength=100,
                      justify='left',
                      anchor='center')

#显示出来
label.pack()

win.mainloop()