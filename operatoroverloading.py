class A:
    def __init__(self, a):
        self.a = a
    def __it__(self, other):
        if(self.a < other.a):
            return True
        else:
            return False
    def __eq__(self, other):
        if self.a == other.a:
            return True
        else:
            return False
        
ob1 = A(2)
ob2 = A(3)
print("The values that have been passed are: ", ob1.a, ob2.a)
print(ob1.a < ob2.a)

ob3 = A(4)
ob4 = A(4)
print("The values that have been passed are: ", ob3.a, ob4.a)
print( ob3 == ob4)