import random
import turtle

turtles = list()

def race():
    global turtles
    winner = False
    finish_line = 590

    while not winner:
        for current_turtle in turtles:
            move = random.randint(0, 18)
            current_turtle.forward(move)

            xcor = current_turtle.xcor()
            if ( xcor >= finish_line ):
                winner = True
                winner_turtle = current_turtle.color()
                print("winner is: ", winner_turtle[0]) # 因為 turtle.color() 會傳傳兩個值我們只須一個就可以

def setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
    screen.bgpic('pavement.gif')

    turtle_ycor = [ -40, -20, 0, 20, 40 ]
    turtle_color = [ 'blue', 'pink', 'purple', 'brown', 'green' ]

    for i in range(0, len(turtle_color)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup() # 將筆提起來
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown() # 將筆放下
        turtles.append(new_turtle)

setup()
race()
turtle.mainloop()
