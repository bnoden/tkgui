import tkinter as tk


title = "test1"
mainwindow = tk.Tk()
mainwindow.title(title)

# mainwindow.resizable(False, False)

label = tk.Label(mainwindow, text="label")

btn = tk.Button(mainwindow, text="button")

label.pack()
btn.pack()

mainwindow.mainloop()
