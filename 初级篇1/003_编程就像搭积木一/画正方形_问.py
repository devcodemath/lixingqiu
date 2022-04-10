from turtle import *

def 画正方形(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for  i in range(4):
        t.fd(100)
        t.right(90)
        
screen = Screen()

t = Turtle()

screen.onclick(画正方形)   # 默认为左键单击,如果是中间则加参数2,右键3
screen.mainloop()


"请增加一个画五角星的函数,单击中键的时候,会在鼠标的坐标画一个五角星"

"请增加一个改变画笔颜色的函数,单击右键的时候,画笔的颜色会变成另一种颜色(可能需要用到全局变量)"
