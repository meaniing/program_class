#6개의 원 그리기

import turtle
t = turtle.Turtle()
t.shape

for i in range(6):
    t.circle(100)
    t.left(360/6)