from Dog import Dog

class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler =  handler
    def walk(self):
        print(self.name, "is helping its handler", self.handler, "walk.")
#def print_dog(dog):
#    print(dog.name + "'s", 'age is', dog.age, 'and weight is', dog.weight)

#jude = Dog('Codie', 12, 38)
#jackson = Dog('Jackson', 9, 12)

#jude.print_dog()
#jackson.print_dog()

#print_dog(codie)
#print_dog(jackson)

#rody =  ServiceDog("Rody", 8, 38, "Jassic")
#print("This dog's name is", rody.name)
#print("This dog's handler is", rody.handler)
#rody.print_dog()
#rody.brak()
#rody.walk()
