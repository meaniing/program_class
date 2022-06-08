#mypaint 프로그램 만들기

from tkinter import *

mycolor = "blue"

def paint (event):
    x1, y1 = ( event.x-1 ), ( event.y+1 )
    x2, y2 = ( event.x-1 ), ( event.y+1 )
    canvas.create_oval( x1, y1, x2, y2, fill = mycolor)

def change_color():
    global mycolor
    mycolor = "red"

window = Tk()
canvas = Canvas (window)
canvas.pack()
canvas.bind("(B1-Motion>", paint)
button = Button(window, text="Z'1", command=change_color)
button.pack()

window.mainloop