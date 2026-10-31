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
win.geometry("1200x700")
win.title("Medical Services")


# Search By Date & Time
the_date_search = StringVar()
Label(win, text="Search Date And Time").place(x=300, y=20)
Entry(win, textvariable=the_date_search).place(x=450, y=20)

# Doctor
doctor = StringVar()
Label(win, text="Doctor").place(x=20, y=60)
Entry(win, textvariable=doctor).place(x=140, y=60)

# The Date
the_date = StringVar()
Label(win, text="Date And Time").place(x=20, y=100)
Entry(win, textvariable=the_date).place(x=140, y=100)

# Service Type
service_type = StringVar()
Label(win, text="Service Type").place(x=20, y=140)
Entry(win, textvariable=service_type).place(x=140, y=140)

# Price
price = IntVar()
Label(win, text="Price").place(x=20, y=180)
Entry(win, textvariable=service_type).place(x=140, y=180)


Button(win, text="Save", width=7,command= save_click).place(x=20,y=600)
Button(win, text="Edit", width=7,command= edit_click).place(x=87,y=600)
Button(win, text="Delete", width=7,command= delete_click).place(x=154,y=600)

table = ttk.Treeview(
    win,
    columns=(1,2,3,4),
    show="headings",
)

table.heading(1, text="Doctor")
table.heading(2, text="Date And Time")
table.heading(3, text="Service Type")
table.heading(4, text="Price")

table.column(1, width=300)
table.column(2, width=180)
table.column(3, width=200)
table.column(4, width=100)

table.place(x=300, y=60)

win.mainloop()
