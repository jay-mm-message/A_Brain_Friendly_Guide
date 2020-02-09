class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_dog(dog):
        print(dog.name + "'s", 'age is', dog.age, 'and weight is', dog.weight)

#def print_dog(dog):
#    print(dog.name + "'s", 'age is', dog.age, 'and weight is', dog.weight)

jude = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 9, 12)

jude.print_dog()
jackson.print_dog()

#print_dog(codie)
#print_dog(jackson)
