from tkinter import *
import tkinter.messagebox
def check():
    n = v.get()
    if n%2==0:
        res.configure(text="Even Number")
    else:
        res.configure(text="Odd Number")
def clear():
    e1.delete(0, END)
def close():
    root.destroy()
def about_author():
    tkinter.messagebox.showinfo("About Me..!!","Hello,this is CHRIAG CHOPRA living in Delhi and currently doing my graduation from PIIT college, Greater Noida \n\n>Instagram : https://www.instagram.com/127.01.0.1/ \t\t>FaceBook : https://www.facebook.com/chirag.chopra.5494")
root = Tk()
root.title("Odd Even Checker by Chirag Chopra V1.1")
root.geometry("340x210")
v = IntVar()
title = Label(root,text="Odd Even Checker",font=("comic sans",12,"bold"))
num = Label(root,text="Enter a Number",font=("comic sans",10,"bold"))
e1 = Entry(root,textvariable=v)
b1 = Button(root,text="Check",bg="#999999",command=check,width=8)
ll = Label(root,text="")
l2 = Label(root,text="     Result          :",font=("comic sans",10,"bold"))
res = Label(root,text="")
b2 = Button(root,text="Exit",bg="#999999",command=close,width=8)
b3=Button(root,text="clear",bg="#999999",command=clear)

title.grid(row=0,column=1)
num.grid(row=1,column=0,sticky=E)
e1.grid(row=1,column=1)
b1.grid(row=2,column=1)
ll.grid(row=3,column=1)
l2.grid(row=6,column=0)
res.grid(row=6,column=1)
b2.grid(row=8,column=2)
b3.grid(row=8,column=1)

line = Menu(root)
root.config(menu=line)

file = Menu(line)
line.add_cascade(label="File", menu=file)
file.add_command(label="About Author", command=about_author)
file.add_command(label="Exit", command=close)
root.mainloop()