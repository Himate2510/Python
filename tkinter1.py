from tkinter import *
window = Tk()
window.title("Simple tiny, easy GUI")
window.geometry("300x300")

hey = Label(text = "Hello", fg = 'black', bg = 'yellow')
button = Button(text = "CLICK THIS BUTTON OR ELSE.......", bg = 'orange', fg = 'Red')
enter = Entry(fg="brown", bg = 'Blue', width = 80)
hey.pack()
button.pack()
enter.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text= "A frame that will end you...")
label.pack()

textbox = Text(fg='black', bg = 'white')
textbox.pack()
window.mainloop()