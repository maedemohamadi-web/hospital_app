from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def save_click():
    pass

def edit_click():
    pass


def delete_click():
    pass

win = Tk()
win.geometry("800x600")
win.title("Patients")


# Search By Code
code_search = IntVar()
Label(win, text="Search Code").place(x=250, y=20)
Entry(win, textvariable=code_search).place(x=330, y=20)

# Name
name = StringVar()
Label(win, text="Name").place(x=20, y=60)
Entry(win, textvariable=name).place(x=90, y=60)

# Family
family = StringVar()
Label(win, text="Family").place(x=20, y=100)
Entry(win, textvariable=family).place(x=90, y=100)

# Code
code = IntVar()
Label(win, text="Code").place(x=20, y=140)
Entry(win, textvariable=code).place(x=90, y=140)

# Age
age = IntVar()
Label(win, text="Age").place(x=20, y=180)
Entry(win, textvariable=age).place(x=90, y=180)

# Gender
gender = StringVar()
Label(win, text="Gender").place(x=20, y=220)
Entry(win, textvariable=gender).place(x=90, y=220)

Button(win, text="Save", width=7,command= save_click).place(x=20,y=500)
Button(win, text="Edit", width=7,command= edit_click).place(x=87,y=500)
Button(win, text="Delete", width=7,command= delete_click).place(x=154,y=500)

table = ttk.Treeview(
    win,
    columns=(1,2,3,4,5),
    show="headings",
)

table.heading(1, text="Name")
table.heading(2, text="Family")
table.heading(3, text="Code")
table.heading(4, text="Age")
table.heading(5, text="Gender")

table.column(1, width=110)
table.column(2, width=150)
table.column(3, width=100)
table.column(4, width=70)
table.column(5, width=80)

table.place(x=250, y=60)

win.mainloop()
