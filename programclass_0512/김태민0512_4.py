#앵그리 터틀 게임 

import turtle
import math

player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()

def turnleftO():
    player.left(5)

def turnright():
    player.right(5)

def fired():
    X = 0
    y = 0
    velocity = 50
    angle = player.heading()
    vx = velocity * math.cos(angle * 3.14 / 180.0)
    vy = velocity * math.sin(angle * 3.14 / 180.0)
    while player.ycor() >= 0:
        VX = VX
        Vy = vy - 10
        X = X + vx
        y = y + vy
        player.goto(x, y)

screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(fire, "space")
screen.listen()