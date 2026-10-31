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
win.geometry("1300x600")
win.title("Visit")


# Search By Patient
the_patient_search = StringVar()
Label(win, text="Search Patient").place(x=370, y=20)
Entry(win, textvariable=the_patient_search).place(x=470, y=20 , width=230)

# Patient
the_patient = StringVar()
Label(win, text="Patient").place(x=20, y=60)
Entry(win, textvariable=the_patient).place(x=120, y=60 , width=230)

#Medical Service
the_medical_service = StringVar()
Label(win, text="Medical Service").place(x=20, y=100)
Entry(win, textvariable=the_medical_service).place(x=120, y=100, width=230)


Button(win, text="Save", width=7,command= save_click).place(x=20,y=500)
Button(win, text="Edit", width=7,command= edit_click).place(x=87,y=500)
Button(win, text="Delete", width=7,command= delete_click).place(x=154,y=500)

table = ttk.Treeview(
    win,
    columns=(1,2),
    show="headings",
)

table.heading(1, text="Patient")
table.heading(2, text="Medical Service")


table.column(1, width=450)
table.column(2, width=450)


table.place(x=370, y=60)

win.mainloop()
