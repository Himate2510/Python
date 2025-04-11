from abc import ABC, abstractmethod

class Parent(ABC):

    def print(self,x):
        print("The value has been passed!", x)
    @abstractmethod
    def print1(self):
        print("We are inside the task!")
class test_class(Parent):
    def print1(self):
        print("We are inside the test_class!")

test_obj = test_class()
test_obj.print(100)
test_obj.print1()