from Dog import Dog
from Frisbee import Frisbee

class FrisbeeDog(Dog):
    def catch(self, frisbee):
        self.frisbee = frisbee

    def bark(self):
        if self.frisbee:
            print(self.name, "I can't bark. I have a frisbee in my mouth.")
        else:
            Dog.bark(self)

    def give(self):
        frisbee = self.frisbee
        self.frisbee = None
        return frisbee

    def __str__(self):
        if self.frisbee:
            return "I'm a dog named " + self.name + " and I have a frisbee."
        else:
            return "I'm a dog named " + self.name + " and I have not a fribee."

    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None
