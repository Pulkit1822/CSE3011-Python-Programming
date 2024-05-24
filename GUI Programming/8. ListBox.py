from tkinter import *

top = Tk()

L1 = Listbox(top)
L1.insert(1, "1. Python")
L1.insert(2, "2. Java")
L1.insert(3, "3. C++")

L1.pack()
top.mainloop()
