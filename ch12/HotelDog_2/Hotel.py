from Dog import Dog

# lists to dictionaries
class Hotel:
    def __init__(self, name):
        self.name = name
        self.kennel = {}

    def check_in(self, dog):
        if isinstance(dog, Dog):
            self.kennel[dog.name] = dog
            print(dog.name, " is checked into ", self.name)
        else:
            print(" Sorry only Dogs are allowd in ", self.name)

    def check_out(self, name):
        if name in self.kennel:
            dog = self.kennel[name]
            del self.kennel[name]
            print(dog.name, " is checked out of ", self.name)
            return dog
        else:
            print(" Sorry, ", name, " is not boarding at ", self.name)
            return None


