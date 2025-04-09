class Private:

    __privatevar = 27

    def __PrivateMethod(self):
        print("I am inside the class Private! :)")

    def HI(self):
        print("The private variable is: ", self.__privatevar)

foo = Private()
foo.HI()
foo.__PrivateMethod()