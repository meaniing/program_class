#스파이럴 그리기

import turtle
t = turtle.Turtle()

colors = ["red", "purple", "blue", "green", "yellow", "orange"]

turtle.bgcolor("black")

t.speed(0)

t.width(3)

length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5