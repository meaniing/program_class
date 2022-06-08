#거북이 경주게임

import random
import turtle

screen = turtle.Screen()
img1 = ㅇ#맥 쓰는데 파일 경로를 어떻게 써야 할지 몰라 비워 둡니다...
img2 = ㅇ
screen.addshape(img1)
screen.addshape(img2)

t1 = turtle.turtle()
t1.shape(img1)
t1.pensize(5)
t1.penup()
t2.goto(-300,0)

t2 = turtle.turtle()
t1.shape(img2)
t1.pensize(5)
t1.penup()
t2.goto(-300,-200)

t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

for i in range(100):
    d1 = random.randint(1, 60)
    t1.forward(d1)
    d2 = random.randint(1, 60)
    t2.forward(d2)