from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("500x500")
def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World2")
B = Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()