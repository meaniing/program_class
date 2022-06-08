#거북이를 랜던하게 움직이자 

import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for i in range(30):
    l = random.randint(1, 100)
    t.forward(l)
    a = random.randint(-180, 180)
    t.left(a)

