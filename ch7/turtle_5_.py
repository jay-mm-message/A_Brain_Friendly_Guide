import turtle

slowpoke = turtle.Turtle()
slowpoke.pencolor('pink')
#slowpoke.shape('turtle')
slowpoke.shape('circle')
slowpoke.penup()
slowpoke.setposition(-120, 0)
slowpoke.pendown()
slowpoke.circle(100)

slowpoke.pencolor('blue')
slowpoke.penup()
slowpoke.setposition(120, 0)
slowpoke.pendown()
slowpoke.circle(100)

turtle.mainloop()
