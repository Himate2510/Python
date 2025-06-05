from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")

def msg():
    messagebox.showwarning("Warning!", "There is a nuke incoming!!!!!!!!!!!!!!!!!!!!!!!!!")

button = Button(root, text="Click me", command=msg)
button.place(x=0, y=0)

root.mainloop()