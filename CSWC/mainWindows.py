#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tkinter
from tkinter import ttk
from ScrolledText import ScrolledText
import os
import tkFileDialog

class MainWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master,width=600,height=220,bg='blue')
        frame.grid(row=0, column=0)
        frame.pack()
        
        #文件标签
        self.labelFile = tkinter.Label(frame,
                                       text='文件',
                                       font=('黑体'),
                                       justify='left',
                                       )
        self.labelFile.place(x=65, y=30)
        
        #文件路径输入文本框
        #绑定变量
        self.fileVar = tkinter.Variable()
        self.fileEntry = tkinter.Entry(frame,textvariable=self.fileVar, width=45)
        self.fileEntry.place(x=140,y=30)
        
        #打开/浏览文件按键
        self.buttonOpenFile = tkinter.Button(frame, text='打开', command=self.openFile)
        self.buttonOpenFile.place(x=480, y=30)
        
        #图片标签
        self.labelPic = tkinter.Label(frame,
                                       text='图片',
                                       font=('黑体'),
                                       justify='left',
                                       )
        self.labelPic.place(x=65, y=90)
        
        #图片路径输入文本框
        #绑定变量
        self.picVar = tkinter.Variable()
        self.picEntry = tkinter.Entry(frame,textvariable=self.picVar, width=45)
        self.picEntry.place(x=140,y=90)
        
        #打开/浏览图片按键
        self.buttonOpenPic = tkinter.Button(frame, text='打开', command=self.openPic)
        self.buttonOpenPic.place(x=480, y=90)
        
        #过滤词标签
        self.labelPic = tkinter.Label(frame,
                                       text='过滤词',
                                       font=('黑体'),
                                       justify='left',
                                       )
        self.labelPic.place(x=50, y=150)
        
        #带滚动条的文本框，用于显示多行过滤词
        st = ScrolledText(frame, width=33, height=3, font=('黑体', 13))
        st.place(x=140,y=150)
        
        #添加过滤词按键
        self.buttonAddWords = tkinter.Button(frame, text='添加', command=self.addWords)
        self.buttonAddWords.place(x=480, y=150)
        
        
    def openFile(self):
        #获取当前程序所在目录路径
        path = os.path.split(os.path.realpath(__file__))[0]
        fileName = tkFileDialog.askopenfilename(initialdir = path,filetypes=[('Word文档', '*.doc;*.docx'), ('文本文件', '*.txt')])
        self.fileVar.set(fileName)
        
    def openPic(self):
        path = os.path.split(os.path.realpath(__file__))[0]
        picName = tkFileDialog.askopenfilename(initialdir = path,filetypes=[('JPEG', '*.jpg;*.jpeg;*.jpe;*.jfif'), ('PNG', '*.png')])
        self.picVar.set(picName)
    
    def addWords(self):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    