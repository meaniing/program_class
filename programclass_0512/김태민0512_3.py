#에스터로이드 게임

import turtle 
import random
import math

p = turtle.Turtle()
p.color("blue")
p.shape("turtle")
p.penup()
p.speed(0)
Screen = p.getscreen()

a1 = turtle.Turtle()
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300, 300), random.randint(-300, 300))

a2 = turtle.Turtle()
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300, 300), random.randint(-300, 300))