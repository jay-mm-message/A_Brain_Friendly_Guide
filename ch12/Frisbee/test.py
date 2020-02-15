from FrisbeeDog import FrisbeeDog
from Frisbee import Frisbee
from Dog import Dog

def test_code():

    jessic = FrisbeeDog('Jessic', 5, 20)
    print(jessic)
    jessic.bark()

    blue_frisbee = Frisbee('blue')
    jessic.catch(blue_frisbee)
    print(jessic)
    jessic.bark()

    frisbee = jessic.give()
    print(frisbee)
    print(jessic)

test_code()
