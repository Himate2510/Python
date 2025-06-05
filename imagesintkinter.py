from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image in Tkinter")
root.geometry("400x400")

upload = Image.open("ufo.png")

image = ImageTk.PhotoImage(upload)

label = Label(root, height = 400, width = 300, image=image)
label.place(x=0, y=0)
label_2 = Label(root, text="This is an image in Tinkinter")
label_2.place(x=0, y=350)

root.mainloop()