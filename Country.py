class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the official language of India")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington D.C. is the capital of USA")
    def language(self):
        print("English is the official language of USA")
    def type(self):
        print("USA is a developed country")

obj_India = India()
obj_usa = USA()

for country in (obj_India, obj_usa):
    country.capital()
    country.language()
    country.type()