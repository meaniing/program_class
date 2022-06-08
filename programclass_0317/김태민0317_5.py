#집 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

S = int(input("집의 크기는 얼마?"))

t.left(60)
t.forward(S)
t.left(240)
t.forward(S)
t.left(330) #지붕

t.forward(S)
t.right(90)
t.forward(S)
t.right(90)
t.forward(S)
t.right(90)
t.forward(S)


