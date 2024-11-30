# coding=utf-8
import random
from tkinter import *
from tkinter import simpledialog,messagebox

def change(event):
    key=event.keycode
    if(key==33 or key==34 or key==49):
        label.configure(text=list[random.randint(0,len(list)-1)].strip('\n'),font=('微软雅黑',96))
    if(key==27 or key==16):
        if(len(list)<4):
            messagebox.showerror('错误','列表长度小于4')
        else:
            tmp=random.sample(list,4)
            label.configure(text=tmp[0].strip('\n')+' '+tmp[1].strip('\n')+'\n'+tmp[2].strip('\n')+' '+tmp[3].strip('\n'),font=('微软雅黑',48))

try:
    with open('names.ini','r',encoding='utf-8') as file:
        list=file.readlines()
except FileNotFoundError:
    messagebox.showerror('错误','没有找到names.ini')
    exit()

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=windll.shcore.GetScaleFactorForDevice(0)

window = Tk()
window.title('随机抽取')
label=Label(window,text='\n\n单抽：按智能笔上下键\n四抽：按智能笔方形键\n\n\n程序设计：github@lilingyun66',font=('微软雅黑',12))
label.pack(pady=10)
window.tk.call('tk', 'scaling', ScaleFactor/75)
window.geometry(str(int(ScaleFactor*5))+'x'+str(int(ScaleFactor*2)))
window.bind("<Key>", change)
window.mainloop()
