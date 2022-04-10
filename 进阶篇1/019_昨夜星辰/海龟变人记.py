"""海龟变人记.py, 本程序是类的继承的例子"""

from turtle import *
 
class Sprite(Turtle):                 #定义一个叫Sprite的类,继承自Turtle
    def __init__(self,image):
        Turtle.__init__(self,shape=image) #让Sprite的形状为image的gif图片
        self.penup()

        
if __name__ == "__main__":

    image = "人.gif"
    screen = Screen()                 # 新建屏幕对象
    screen.title("海龟变人记")        # 给屏幕的窗口设定标题
    screen.addshape(image)            # 增加gif图到屏幕

    p= Sprite(image)                  # 实例化Sprite对象
    p.goto(-100,100)                  # 定位到(-100,100)的位置
     
    for i in range(4):                # 迭代i变量4次
        p.stamp()                     # 图章
        p.fd(200)                     # 前进200个单位
        p.rt(90)                      # 右转90度

    screen.exitonclick()              # 单击屏幕关闭窗口
