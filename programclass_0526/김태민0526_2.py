#절대위치배치관리자

from tkinter import *

window = Tk()

W = Label(window, text = "박스 #1", bg = "red", fg = "white")
W.place(x = 0, y = 0)

W = Label (window, text="박스 #2", bg="green", fg="black")
W.place(x=20, y=20)

W = Label(window, text="박스 #3", bg="blue", fg="white")
W.place(x=40, y=40)

window.mainloop()