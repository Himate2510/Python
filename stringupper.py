class Upper():
    def __init__(self):
        self.Lower = ""

    def get(self):
        self.Lower = input("Enter a string value... (Or get nuked... :))_ :")
    
    def prints(self):
        print("The result of the string in upper case is...: ", self.Lower.upper())

obj = Upper()

obj.get()
obj.prints()