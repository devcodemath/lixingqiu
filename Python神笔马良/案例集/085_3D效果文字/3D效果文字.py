"""
   3D效果文字.py
"""
import turtle

# 给Turtle类增加addx和addy方法
turtle.Turtle.addx = lambda self,dx:self.setx(self.xcor() + dx)
turtle.Turtle.addy = lambda self,dy:self.sety(self.ycor() + dy)

zt = ('微软雅黑',42,'normal')
string = '风火轮编程'

tom = turtle.Turtle(visible=False)
tom.penup()

tom.color('black')
for _ in range(5):
    tom.addx(-1)                           # x坐标减1
    tom.addy(1)                            # y坐标加1 
    tom.write(string,align='center',font=zt)

tom.color('blue')
tom.write(string,align='center',font=zt)
tom.screen.mainloop()
