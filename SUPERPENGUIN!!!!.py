class Bird:
    def __init__(self):
        print("Hey I am a bird")
    def Whooisthis(self):
        print("BIRDY")

    def fly(self):
        print("Hey I cant fly! How rude!")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Hey guys! Me penguin!")

    def Whooisthis(self):
        print("What do you think? I AM A PENGUIN DOOFUS!")
    def BecomeHelicopter(self):
        print(" I CANT BECOME A HELICOPTER!!! I CANT EVEN FLY!!!!")


peggy = Penguin()
peggy.Whooisthis()
peggy.fly()
peggy.BecomeHelicopter()
