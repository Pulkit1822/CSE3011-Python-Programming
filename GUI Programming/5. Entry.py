from tkinter import *

top = Tk()

L1 = Label(top, text="User Name")
L1.grid(row=0, column=0)
L2 = Label(top, text="Password")
L2.grid(row=1, column=0)

E1 = Entry(top, bd=5)
E1.grid(row=0, column=1)
E2 = Entry(top, bd=5)
E2.grid(row=1, column=1)

top.mainloop()
