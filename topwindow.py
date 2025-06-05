from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Hello")

def topwindow():
    top = Toplevel()
    top.geometry("200x200")
    top.title("Top Window")
    label2 = Label(top, text = "This is the top level window.")
    label2.pack()


    top.mainloop()

label = Label(root, text = "This is the root window.")
button = Button(root, text = "Want to open another window? Click here!", command = topwindow)

label.pack()
button.pack()

root.mainloop()