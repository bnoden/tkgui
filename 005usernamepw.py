from tkinter import *  # Don't do this


mainwindow = Tk()

Label(mainwindow, text="Username").grid(row=0, sticky=W)
Label(mainwindow, text="Password").grid(row=1, sticky=W)

Entry(mainwindow).grid(row=0, column=1, sticky=E)
Entry(mainwindow).grid(row=1, column=1, sticky=E)

Button(mainwindow, text="Login").grid(row=2, column=1, sticky=E)

mainwindow.mainloop()
