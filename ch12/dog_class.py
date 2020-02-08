
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def brak(self):
        if self.weight > 15:
            print(self.name, " WOW WOW")
        else:
            print(self.name, " wow wow")
    def how_old(self):
        print(self.name, " it's ", self.age, " year old.")

codie = Dog("Codie", 12, 38)
jackson = Dog("Jackson", 9, 12)

codie.how_old()
jackson.how_old()

codie.brak()
jackson.brak()