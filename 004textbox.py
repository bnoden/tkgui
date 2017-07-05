import tkinter as tk
from tkinter import ttk

mainwindow = tk.Tk()

mainwindow.title("Textbox")

label1 = ttk.Label(mainwindow, text="Label")
label1.grid(column=0, row=0)


def pushbutton():
    act.configure(text="Hi " + name.get())

ttk.Label(mainwindow, text="User Name:").grid(column=0, row=0)

name = tk.StringVar()  # Tkinter isn't dynamically typed like Python proper
name_entered = ttk.Entry(mainwindow, width=24, textvariable=name)
name_entered.grid(column=0, row=1)

act = ttk.Button(mainwindow, text="button", command=pushbutton)
act.grid(column=1, row=1)

mainwindow.mainloop()
