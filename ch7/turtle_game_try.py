import turtle
import random

turtles = list()

def race():
    global turtles
    finish_line = 590
    winner = False

    while not winner:
        for current_turtle in turtles:
            move = random.randint(0, 17)
            current_turtle.forward(move)

            xcor = current_turtle.xcor()
            if ( xcor >= finish_line ):
                winner = True
                winner_color = current_turtle.color()
                print("Winner is: ", winner_color[0])

def setup():
    global turtles
    start_line = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
    screen.bgpic('pavement.gif')

    turtle_ycor = [ -40, -20, 0, 20, 40 ]
    turtle_color = [ 'blue', 'purple', 'pink', 'brown', 'green' ]

    for i in range(0, len(turtle_color)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(start_line, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()

        turtles.append(new_turtle)

setup()
race()
turtle.mainloop()
