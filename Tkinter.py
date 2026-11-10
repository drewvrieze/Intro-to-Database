from tkinter import *
from tkinter import ttk
from db import *



def answer():
    print("answer")

def callback():
    print("callback")


def clickHandler(first:StringVar,last:StringVar,phone:StringVar,major:StringVar):
    print(first,last,phone,major)

root = Tk()

frm = Frame(root)
frm.grid()

Label(frm, text = "First Name").grid(column = 0, row = 0)
strFirst = StringVar()
Entry(frm, textvariable=strFirst).grid(column = 1, row = 0)

Label(frm, text = "Last Name").grid(column = 0, row = 1)
strLast = StringVar()
Entry(frm, textvariable=strLast).grid(column = 1, row = 1)

Label(frm, text = "Phone").grid(column = 0, row = 2)
strPhone = StringVar()
Entry(frm, textvariable=strPhone).grid(column = 1, row = 2)

Label(frm, text = "Major").grid(column = 0, row = 3)
strMajor = StringVar()
Entry(frm, textvariable=strMajor).grid(column = 1, row = 3)

Label(frm, text = "Comments").grid(column = 0, row = 3)
strComments = StringVar()
Text(frm, textvariable=strComments).grid(column = 1, row = 3)



Button(frm, text = "Add Student", command = lambda :clickHandler(strFirst,strLast,strPhone,strMajor,strComments)).grid(column = 0, row = 5)
Button(frm, text = "Cancel", command = quit).grid(column = 1, row = 5)



# Button(text = 'Button1', command = callback).pack(fill = tk.X)
# Button(text = 'Button2', command = answer).pack(fill = tk.X)
# Entry(text = "Hello").grid(column = 3, row = 0)
root.mainloop()




