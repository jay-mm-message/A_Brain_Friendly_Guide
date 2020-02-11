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

    def print_dog(self):
            print(self.name + "'s", 'age is', self.age, 'and weight is', self.weight)

class Service_Dog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler =  handler
        self.is_working = False

    def walk(self):
        print(self.name, "is helping its handler", self.handler, "walk.")

    def brak(self):
        if self.is_working:
            print(self.name, "says, I can't bark, I'm working")
        else:
            Dog.brak(self)
#def print_dog(dog):
#    print(dog.name + "'s", 'age is', dog.age, 'and weight is', dog.weight)

#jude = Dog('Codie', 12, 38)
#jackson = Dog('Jackson', 9, 12)

#jude.print_dog()
#jackson.print_dog()

#print_dog(codie)
#print_dog(jackson)

rody =  Service_Dog("Rody", 8, 38, "Jassic")
print("This dog's name is", rody.name)
print("This dog's handler is", rody.handler)
rody.print_dog()

work_state = input("It's working now: (True or False) ")
if work_state == "True":
    rody.is_working = True

rody.brak()
rody.walk()
