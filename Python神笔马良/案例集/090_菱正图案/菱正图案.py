"""
   菱正图案.py
   本程序把所定义的函数和下一行代码去掉，也能运行，但有什么区别?
   请仔细观察！
"""
import turtle

def _createline(self):
    """在画布上创建不可见的线条项目
    """
    return self.cv.create_line(0, 0, 0, 0, fill="",
             width=2,capstyle=turtle.TK.BUTT,joinstyle=turtle.TK.MITER)

turtle.TurtleScreenBase._createline = _createline

turtle.bgcolor('white')
turtle.pensize(10)
turtle.hideturtle()                    # 隐藏海龟
turtle.pencolor('#eE00e6')

turtle.circle(100,360,4)
turtle.penup()
turtle.sety(turtle.ycor()+40)          # y坐标增加40

turtle.pensize(20)                     # 画笔粗细为20 
turtle.pendown()                       # 落笔
turtle.circle(60,360,4)                

turtle.done()                          # 事件循环
