import tkinter as tk
from tkinter import ttk


title = "test2"
mainwindow = tk.Tk()
mainwindow.title(title)

ttk.Label(mainwindow, text="Lookie at this here label").grid(column=8, row=8)

# btn = tk.Button(mainwindow, text="button")

# btn.pack()

mainwindow.mainloop()
