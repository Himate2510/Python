import random
import time
number = random.randint(1, 10)

def intro():
    print("Hello! What is your name?")
    global name
    name = input()
    print("Hello,"+ name + "! I am thinking of a number between 1 and 1000.")
    print("Try to guess the number in 1000 attempts.")
    if(number%2 == 0):
        print("Hint: The number is even.")
    else:
        print("Hint: The number is odd.")
    time.sleep(1.9999999)
    print("Guess the number!")

def totalguess():
    guessesTaken = 0
    while guessesTaken < 1000:
        guess = input("Enter your guess! (Or you will be nuked.)")
        try:
            guess = int(guess)
            if guess<=10 and guess>=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<=1000:

                    if guess < number:
                        print("Your guess is too low.")
                    if guess > number:
                        print("Your guess is too high. You shall now be nuked.")
                    if guess != number:
                        print("Try again, or a bomb will be dropped on you")
                    if guess == number:
                        break
            if guess>1000 or guess<1:
                print("You are out of range. A tank shall now arrive at your location and destroy you!")
        except:
            print("How dare you not insert a number?! You shall be blasted by a nuke.")
    if guess == number:
        print("You got the number in", guessesTaken, "attempts!, now do it again and improve your score or a tank will be coming to you.")
    if guess != number:
        print("You have failed to guess the number in 1000 attempts, how could you? You had 1000 attempts!!!!!!!!!!")
playagain = "yes"
while playagain == "yes" or playagain == "Yes" or playagain == "Y":
    intro()
    totalguess()   
    print("Do you want to play again? (Yes or no?)(You better or something will hit you when you least expect it....)")
    playagain = input()
