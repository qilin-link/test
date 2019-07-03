#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter
import os
from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title('TreeFile')
win.geometry('600x400+200+50')

path = 'D:\\script'

infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)





win.mainloop()