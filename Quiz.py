import random
class fruitquizz:
    def __init__(self):

        self.fruits={"Apple": "red",
                        "Banana": "yellow",
                        "Grapes": "purple",
                        "Orange": "orange",
                        "Watermelon": "green",
                        "Pineapple": "brown",
                        "Strawberry": "red",
                        "Blueberry": "blue",
                        "Mango": "yellow",
                        "Kiwi": "green"}
        
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print(f"What color is {fruit}?")
            user_answer = input()

            if (user_answer.lower()==color):
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is {color}.")
            option = int(input("enter 0, if you want to play again, else enter 1"))
            if (option == 1):
                break
            else:
                continue
print("welcome to the fruit quiz!!!!!!!!!!!!!!!!!!!!!!")
fq = fruitquizz()
fq.quiz()        