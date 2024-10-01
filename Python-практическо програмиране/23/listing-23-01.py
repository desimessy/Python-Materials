from tkinter import *
from tkinter.filedialog import *
import fileinput
 
def _open():
     global txt
     op = askopenfilename()
     print(op)
     f = open(op, "r", encoding='utf-8')
     content = f.read()
     txt.delete(1.0,END)
     txt.insert(END, content)


root = Tk()
 
m = Menu(root)
root.config(menu=m)
 
fm = Menu(m)
m.add_cascade(label="File",menu=fm)
fm.add_command(label="Open...",command=_open)
 
txt = Text(root,width=40,height=15,font="Courier 10")
txt.pack()
 
root.mainloop()
