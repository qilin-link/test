#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter
from tkinter import ttk
import os

class LowWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master,width=600,height=80,bg='yellow')
        frame.grid(row=1, column=0)
        frame.pack()
        #创建按钮
        self.buttonCreate = tkinter.Button(frame, text='生成', command=self.makeWordsCloud)
        self.buttonCreate.place(x=180, y=20)

        self.buttonQuit = tkinter.Button(frame, text='退出', command=frame.quit)
        self.buttonQuit.place(x=400, y=20)

    
    #制作词云图方法    
    def makeWordsCloud(self):
        pass