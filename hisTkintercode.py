from tkinter import *
from tkinter import ttk
def clickHandler(first,last,phone,major,comments):  # This expects 4 stringVar
    print(first,last,phone,major,comments)
    #insertStudent(.....)

root = Tk()
frm = Frame(root)
frm.grid()

Label(frm, text="First Name").grid(column=0, row=0)
first=StringVar()
Entry(frm,textvariable=first).grid(column=1,row=0)

Label(frm, text="Last Name").grid(column=0, row=1)
last=StringVar()
Entry(frm,textvariable=last).grid(column=1,row=1)

Label(frm, text="Phone").grid(column=0, row=2)
phone=StringVar()
Entry(frm,textvariable=phone).grid(column=1,row=2)

Label(frm, text="Major").grid(column=0, row=3)
major=StringVar()
Entry(frm,textvariable=major).grid(column=1,row=3)

Label(frm, text="Comments").grid(column=0, row=4)
comments=Text(frm,height=2, width=30)
comments.grid(column=1,row=4)

Button(frm, text="Add Student", command=lambda :clickHandler(
      first.get(),
      last.get(),
      phone.get(),
      major.get(),
      comments.get("1.0",END))).grid(column=0, row=5)
Button(frm, text="Cancel", command=quit).grid(column=1, row=5)
root.mainloop()