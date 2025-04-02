class guy:

    def __init__(self, name, Identification_Number):
        self.name = name
        self.Identification_Number = Identification_Number

    def This_Print(self):
        print("The name of the guy is:", self.name)
        print("The Identification Number of the guy is:", self.Identification_Number)

class Employee(guy):
    def __init__(self, name, Identification_Number, Post, Salary):
        self.Salary = Salary
        self.Post = Post
        guy.__init__(self, name, Identification_Number)
   
Hi = Employee("Jeff", 1233241, "Manager", 1000000)

Hi.This_Print()
print (Hi.Post)
print (Hi.Salary)
print (Hi.name)
print (Hi.Identification_Number)

