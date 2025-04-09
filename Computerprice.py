class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("The selling price of the given PC is: {}".format(self.__maxprice))
    
    def setMaxPrice(self, price):
        self.__maxprice = price

PC = Computer()
PC.sell()

PC.__maxprice = 1000
PC.sell()

PC.setMaxPrice(1000)
PC.sell()