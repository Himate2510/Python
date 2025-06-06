from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('The denomination calculator... :))) (Hope it works.)')
root.geometry("500x500")
root.configure(bg = 'Blue')

upload = Image.open("OIP.jpg")
upload = upload.resize((400, 400))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image)
label.place(x=0, y=0)

label2 = Label(root, text = "Welcome to the Demonination Calculator! Hope that it works because it rarely does!", bg = 'Red')

label2.place(x=0, y=200)

def msg():
    MsgBox = messagebox.showinfo(
        "ALERT!","Do you want to calculate the count?")
    if MsgBox == "ok":
        topwin()

button1 = Button(root, text="Click me to get started with the calculations!",
                  command=msg, bg='brown', fg='White')
button1.place(x=5, y=387)

def topwin():
    top = Toplevel()
    top.title("Calculator of Denominatons")
    top.geometry("500x600+100+100")
    top.configure(bg='Dark Blue')

    label4 = Label(top, text="Enter the total amount of money:" , bg='Black', fg="White")
    entry = Entry(top)
    label5 = Label(top, text="Here is the number of note for each of the denomination's : ", bg = 'White')

    l1 = Label(top, text="2000", bg = "White")
    l2 = Label(top, text="500", bg = "White")
    l3 = Label(top, text="100", bg = "White")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount  %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0,str(note2000))
            t2.insert(0, str(note500))
            t3.insert(0, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    btn = Button(top, text="Caculate", command=calculator, bg="brown", fg="white")

    label4.place(x=10, y=10)
    entry.place(x=10, y=40)
    btn.place(x=10, y=70)
    label5.place(x=10, y=100)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()
root.mainloop()