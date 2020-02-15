class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return "I'm a " + self.name + " dog."

    def bark(self):
        if self.weight > 10:
            print(self.name, "say WOW WOW.")
        else:
            print(self.name, "say wow wow.")
