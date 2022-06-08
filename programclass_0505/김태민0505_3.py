#클릭 하는 곳에 사각형 그리기
import turtle # 터틀 그래픽 모듈을 포함한다.
t = turtle.Turtle()
 
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
        
def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill() # 색채우기 위해서 필요하다
    t.color("green")
    square(50)
    t.end_fill() # 색채우기 위해서 필요하다
 
s = turtle.Screen() # 그림이 그려지는 화면을 얻는다.
s.onscreenclick(drawit) # 마우스 클릭 이벤트 처리 함수를 등록한다