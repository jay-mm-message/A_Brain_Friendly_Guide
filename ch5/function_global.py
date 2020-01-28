
greeting = 'Greetings'

def greet(name, message):
    global greeting

    greeting = 'Hi'
    print('<function>', greeting, name + '.', message)


print('<global> ', greeting)
greet('June', 'See you soon!')
print('<global> ', greeting)
