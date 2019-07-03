#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter
from tkinter import ttk
import os
from mainWindows import MainWindows
from lowWindows import LowWindows

win = tkinter.Tk()
win.title('词云生成器')
win.geometry('600x300+400+200')

mainWin = MainWindows(win)
lowWin = LowWindows(win)





win.mainloop()