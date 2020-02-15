from Dog import Dog

class Hotel:
    def __init__(self, name):
        self.name = name
        self.kennel_names = []
        self.kennel_dogs = []

    def check_in(self, dog):
        if isinstance(dog, Dog):
            self.kennel_names.append(dog.name)
            self.kennel_dogs.append(dog)
            print(dog.name, " is checked into ", self.name)
        else:
            print(" Sorry only Dogs are allowd in ", self.name)

    def check_out(self, name):
        for i in range(0, len(self.kennel_names)):
            if name == self.kennel_names[i]:
                dog = self.kennel_dogs[i]
                del self.kennel_names[i]
                del self.kennel_dogs[i]
                print(dog.name, " is checked out of ", self.name)
                return dog
        print(" Sorry, ", name, " is not boarding at ", self.name)
        return None


