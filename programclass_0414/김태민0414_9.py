#사각형 그리기

import turtle
t = turtle.Turtle()
t.shape("turtle")

n = 0

while n < 4:
    t.forward(100)
    t.left(90)
    n = n + 1
