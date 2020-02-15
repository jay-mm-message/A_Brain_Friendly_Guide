from Hotel import Hotel
from Dog import Dog
from Cat import Cat
from ServiceDog import ServiceDog

def test_code():
    codie = Dog("Codie", 12, 38)
    jackson = Dog("Jackson", 9, 12)
    sparky = Dog("Sparkey", 2, 14)
    rody = ServiceDog("Rody", 8 , 38, "Joseph")
    kitty = Cat("Kitty")

    hotel = Hotel("Doggie Hotel")
    hotel.check_in(codie)
    hotel.check_in(jackson)
    hotel.check_in(sparky)
    hotel.check_in(rody)
    hotel.check_in(kitty)

    dog_name = codie.name
    dog = hotel.check_out(dog_name)
    if dog:
        print("Checkout out ", dog.name, " who is ", dog.age, " and ", dog.weight, " lbs ")
    dog_name = jackson.name
    dog = hotel.check_out(dog_name)
    if dog:
        print("Checkout out ", dog.name, " who is ", dog.age, " and ", dog.weight, " lbs ")
    dog_name = sparky.name
    dog = hotel.check_out(dog_name)
    if dog:
        print("Checkout out ", dog.name, " who is ", dog.age, " and ", dog.weight, " lbs ")
    dog_name = rody.name
    dog = hotel.check_out(dog_name)
    if dog:
        print("Checkout out ", dog.name, " who is ", dog.age, " and ", dog.weight, " lbs ")
    dog_name = kitty.name
    dog = hotel.check_out(dog_name)
    if dog:
        print("Checkout out ", dog.name, " who is ", dog.age, " and ", dog.weight, " lbs ")

test_code()
