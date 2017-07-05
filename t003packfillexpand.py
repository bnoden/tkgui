from tkinter import *  # Don't do this


mainwindow = Tk()

frame = Frame(mainwindow)

# side and fill
Label(frame, text="Pack side and fill").pack()

Button(frame, text="1").pack(side=LEFT, fill=Y)
Button(frame, text="2").pack(side=TOP, fill=X)
Button(frame, text="3").pack(side=RIGHT, fill=NONE)
Button(frame, text="4").pack(side=TOP, fill=BOTH)

frame.pack()
# top frame does not expand or fill in
# X or Y directions
# demo of expand options - best understood by expanding the root
# widget and seeing the effect on all the three buttons below.
Label(mainwindow, text="Pack expand").pack()
Button(mainwindow, text="No expand").pack()
Button(mainwindow, text="No fill, yes expand").pack(expand=1)
Button(mainwindow, text="Yes fill, yes expand").pack(fill=X, expand=1)

mainwindow.mainloop()
