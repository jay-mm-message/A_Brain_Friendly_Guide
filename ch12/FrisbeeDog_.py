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
            print(self.name, "says WOW WOW")
        else:
            print(self.name, "says wow wow")

class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee:
            print(self.name, "says, I can't bark, I have a frisbee in my mouth")
        else:
            Dog.brak(self)

    def catch(self, frisbee):
        self.frisbee = frisbee

    def give(self):
        if self.frisbee:
            print(self.name, "caught", self.frisbee)

    def __str__(self):
        return "I'm a dog named " + self.name

# test
def test_code():
    dude = FrisbeeDog("Dude", 5, 11)
    blue_frisbee = Frisbee("blue")

    print(dude)
    dude.bark()
    dude.catch(blue_frisbee)
    frisbee = dude.give()
    dude.bark()
    print(blue_frisbee)
    print(dude)

# main
test_code()
