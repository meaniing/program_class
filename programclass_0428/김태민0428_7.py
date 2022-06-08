#시계 그리기

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.stamp()
move = 30

for i in range(12):
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(25)
    t.penup()
    t.forward(15)
    t.stamp()
    t.home()
    t.right(move)
    move = move + 30