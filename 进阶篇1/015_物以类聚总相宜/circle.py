"""circle.py,本程序定义了一个圆类。"""

class Circle:
    def __init__(self,position,radius):
        """position：圆的中心点坐标,radius：半径"""
        self.center = position
        self.radius = radius

    def area(self):
        """计算圆的面积"""
        return self.radius**2*3.1415926
    
    def perimeter(self):
        """计算圆的周长"""
        return 2*self.radius*3.1415926


p = (200,200)
r = 50
c1 = Circle(p,r)
print("c1的面积是:",c1.area())
print("c1的周长是:",c1.perimeter())

"请用turtle把实例化的圆形画出来，以下是参考代码："

from turtle import Turtle

t = Turtle(visible=False)
t.penup()
t.goto(c1.center)
t.fd(c1.radius)
t.left(90)
t.pendown()
t.circle(c1.radius)
