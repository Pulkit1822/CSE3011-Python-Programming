from tkinter import *

top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Option 1", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
C2 = Checkbutton(top, text = "Option 2", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
C1.pack()
C2.pack()
top.mainloop()