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
win.geometry("1000x500")
win.title("Doctors")


# Search By Medical Council Number
medical_council_number_search = StringVar()
Label(win, text="Search Medical Council No").place(x=300, y=20)
Entry(win, textvariable=medical_council_number_search).place(x=450, y=20)

# The Name
the_name = StringVar()
Label(win, text="Name").place(x=20, y=60)
Entry(win, textvariable=the_name).place(x=140, y=60)

# The Family
the_family = StringVar()
Label(win, text="Family").place(x=20, y=100)
Entry(win, textvariable=the_family).place(x=140, y=100)

# Specialization
specialization = StringVar()
Label(win, text="Specialization").place(x=20, y=140)
Entry(win, textvariable=specialization).place(x=140, y=140)

# Medical Council Number
code = StringVar()
Label(win, text="Medical Council No").place(x=20, y=180)
Entry(win, textvariable=code).place(x=140, y=180)


Button(win, text="Save", width=7,command= save_click).place(x=20,y=400)
Button(win, text="Edit", width=7,command= edit_click).place(x=87,y=400)
Button(win, text="Delete", width=7,command= delete_click).place(x=154,y=400)

table = ttk.Treeview(
    win,
    columns=(1,2,3,4),
    show="headings",
)

table.heading(1, text="Name")
table.heading(2, text="Family")
table.heading(3, text="Specialization")
table.heading(4, text="Medical Council No")

table.column(1, width=150)
table.column(2, width=150)
table.column(3, width=180)
table.column(4, width=200)

table.place(x=300, y=60)

win.mainloop()
