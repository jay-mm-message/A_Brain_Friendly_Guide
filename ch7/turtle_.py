import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')

for i in range(0, 12, 1):
    if i == 1 or i == 5 or i == 9:
        slowpoke.color('blue')
    elif i == 2 or i == 6 or i == 10:
        slowpoke.color('red')
    elif i == 3 or i == 7 or i == 11:
        slowpoke.color('green')
    elif i == 4 or i == 8 or i == 12:
        slowpoke.color('pink')
    else:
        slowpoke.color('black')

    slowpoke.forward(100)
    slowpoke.right(30)

slowpoke.left(90)

turtle.mainloop()
