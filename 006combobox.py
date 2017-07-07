import tkinter as tk
from tkinter import ttk

mainwindow = tk.Tk()

mainwindow.title("Combo box")

label1 = ttk.Label(mainwindow, text="Label")
label1.grid(column=0, row=0)

name = tk.StringVar()  # Tkinter isn't dynamically typed like Python proper
fontsize = tk.StringVar()


def pushbutton():
    act.configure(text="Size: " + fontsize.get())

# ------------------- Textbox ---------------------------
ttk.Label(mainwindow, text="User Name:").grid(column=0, row=0)

name_entered = ttk.Entry(mainwindow, width=24, textvariable=name)
name_entered.grid(column=0, row=1)

act = ttk.Button(mainwindow, text="button", command=pushbutton)
act.grid(column=2, row=1)
# -------------------------------------------------------

# -------------------- Combo box ------------------------
ttk.Label(mainwindow, text="Size:").grid(column=1, row=0)

fontsize_selected = ttk.Combobox(mainwindow,
                                 width=12, textvariable=fontsize)
fontsize_selected['values'] = (6, 8, 10, 12, 14, 16, 18, 20,
                               22, 24, 28, 32, 36, 40, 48)
fontsize_selected.grid(column=1, row=1)
fontsize_selected.current(0)
# --------------------------------------------------------

name_entered.focus()

mainwindow.mainloop()
