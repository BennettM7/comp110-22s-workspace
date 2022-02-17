from turtle import Turtle, colormode, done
colormode(255)
bob: Turtle = Turtle()
bob.color(99, 204, 250)
bob.penup()
bob.goto(-100, -45)
bob.pendown()
bob.fillcolor(120, 0, 255)
bob.begin_fill()
i: int = 0
SIDE_LENGTH: int = 200
ANGLE: int = 120
while (i < 3):
    bob.forward(SIDE_LENGTH)
    bob.left(ANGLE)
    i += 1
bob.end_fill()
done()