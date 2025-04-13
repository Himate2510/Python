class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+' ( '+self.meaning+')'

flash = []
print("Weelcome to the flashcard application!! Good luck!")

while(True):
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")
    flash.append(flashcard(word, meaning))
    option = int(input("Enter 1, if you want to add another flashcard to your deck, if not press 0. (I suggest pressing one or you get nuked.. :)))) :"))
    if(option == 0):
        break
print("\n Your flashcards")
for i in flash:
    print(">", i)
    