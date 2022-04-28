###################################
#      Made by Erfan Sadeghi      #
###################################

import tkinter as tk
from tkinter import messagebox
from pyttsx3 import speak
from time import localtime
from random import choice

root = tk.Tk()
root.tk.call('tk', 'scaling', 3.0)
weword = open('word_hard.txt','a',encoding="utf8")
def show_info():
    messagebox.showinfo('error', 'این کلمه قبلا سخت انتخاب شده!')
wordh = open('word_hard.txt',encoding="utf8")
namej = wordh.readlines()
def sakht():
    for i in namej :
        if i.strip()[0:i.find(':')] == name[0:eng] :
            show_info()
            return
    chap = str(name)+'\n'
    weword.writelines(str(chap))
    weword.close()
def speek():
    speak(name[0:eng])

roz = localtime()
roz = roz.tm_yday
frr = open('setting.txt' , 'r')
fa = open('english_text.txt' ,'a+',encoding="utf8")
file = open('english_text.txt' , encoding="utf8" )
fr = file.readlines()
sf = frr.readlines()
emroz = sf.pop()
emroz = int(emroz[7:])
level = sf.pop()
x = int(level[7:])
if emroz == roz:
    x=x-1
name = fr[x].strip()
eng = name.find(':')
if roz%3==0:
    name = choice(namej)
    name = name.strip()
    if emroz != roz:
        x=x-1
x = x+1
height = (len(name))
height = height*30

fw = open('setting.txt' , 'w')
fw.write('level :%i\ntoday :%i' %(int(x),int(roz)))

label = tk.Label(root, text = str(name))
label.pack(padx = 5, pady = 5)
tk.Button(root,text='تلفظ',font=('bnazanin',10) , command=speek).pack()
tk.Button(root,text='کلمه سخته' ,font=('bnazanin',10),command=sakht).pack()
root.geometry("%ix200" %height)
root.mainloop()
