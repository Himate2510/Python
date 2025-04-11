from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Snake(Animal):
    
        def move(self):
            print("I slither on the ground.")

class Human(Animal):
        
        def move(self):
            print("I walk on two legs.")

class Nuke(Animal):
     def move(self):
          print("I get dropped from a plane and explode citys. :)")

R = Human()
R.move()

S = Snake()
S.move()

N = Nuke()
N.move()
