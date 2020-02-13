class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "I'm a " + self.color + ' frisbee'

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def brak(self):
        if self.weight > 15:
            print(self.name, "WOW WOW")
        else:
            print(self.name, "wow wow")

class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee:
            print("I can't bark, I have a frisbee in my mouth")
        else:
            Dog.brak(self)

    def catch(self, frisbee):
        self.frisbee = frisbee

    def give(self):
        if self.frisbee:
            print(self.frisbee)
        self.frisbee = None

    def __str__(self):
        return "I'm a FrisbeeDog class."

# test
def test_code():
    dude = FrisbeeDog("Dude", 5, 20)
    blue_frisbee = Frisbee("Blue")

    print(dude)
    dude.bark()
    dude.catch(blue_frisbee)
    dude.bark()
    print(dude)
    frisbee = dude.give()
    print(frisbee)
    print(dude)

# main
test_code()
