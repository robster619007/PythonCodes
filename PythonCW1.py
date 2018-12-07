#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Mon Nov 26 14:36:00 2018

@author: robeeghosh
"""
import json 
from tkinter import *
from urllib.request import urlopen 

with urlopen("http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/issuu_sample.json") as response:
    src = response.read()


print(src)



root = Tk()
root.geometry('400x400+200+200')
root.title("CW1 Data Reader")

frame = Frame(root)
frame.pack()

Visitor_uid = Label(frame,text = "Visitor id:")
Visitor_Entry = Entry(frame)
Visitor_uid.grid(row = 0,sticky = E)
Visitor_Entry.grid(row = 0, column = 1)
button1 = Button(frame, text="Find",fg = "RED")
button1.grid(row = 1,column = 1)


root.mainloop()

'''



button2 = Button(topFrame, text="World", fg = "green")
button3 = Button(topFrame, text="Robee", fg = "purple")
button4 = Button(bottomFrame, text="Here", fg = "blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

'''

"""
theLabel = Label(root, text = "Hello World")
theLabel.pack()


"""

