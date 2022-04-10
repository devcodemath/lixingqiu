"""旋转的三角形-按空格键跳.py ,本程序设计了继承自海龟的Triangle类。
实例化对象后可以用鼠标指针拖动它,并且它会自动旋转。
在屏幕上单击鼠标右键它能归位。按空格键后，它们都会跳起来。"""

from turtle import *
 
class Triangle(Turtle):
    counter = 0                        # 实例对象计数器
    jec = 0                            # 已跳完归位数量
    def __init__(self,color,position):
        Turtle.__init__(self,shape='triangle')
        self.初始坐标 = position       # 记录初始坐标
        self.shapesize(2,2)            # 放大2倍
        self.penup()                   # 抬笔
        self.goto(position)            # 定位
        self.color(color)              # 设定颜色
        self.ondrag(self.goto)         # 拖放到
        self.rotate()                  # 旋转
        self.yspeed = 0                # 垂直速度
        self.aspeed = 0                # 加速度
        Triangle.counter +=1           # 统计数量
        
    def rotate(self):
        """旋转方法"""
        self.right(2)
        screen.ontimer(self.rotate,10)
        
    def jump(self):
        self.aspeed = -1              # 加速度设为-1
        self.yspeed = 15              # 初始垂直速度设为15
        self.oldy = self.ycor()       # 记录初始y坐标
        self.move()                   # 开始移动
        
    def move(self):
        """让对象在受到重力的情况下跳起来"""
        self.sety(self.ycor() + self.yspeed)    # 上移
        if self.ycor() > self.oldy:             # y坐标大于起始y坐标
            self.yspeed = self.yspeed + self.aspeed # y速度变化
            self.screen.ontimer(self.move,50)       # 继续调用move
        else:                                       # 否则就是落下来了
            self.sety(self.oldy)                # 回到原来的y坐标
            "由于是异步跳，通过计次判断是否全部跳完了，才能重新绑定"
            Triangle.jec +=1                    # 跳完了，统计下
            if Triangle.jec == Triangle.counter:# 全都跳完会等于counter
                self.screen.onkey(jump,"space") # 重新绑定空格键到jump
      
        
def reset(x,y):
    """回到初始位置，面向右的方向"""
    [t.goto(t.初始坐标) for t in screen.turtles()]
    [t.setheading(0) for t in screen.turtles()]
    
def jump():
    """按空格键让所有三角形都跳起来"""
    screen.onkey(None,"space")   # 松绑
    Triangle.jec = 0             # 开始计次
    [t.jump() for t in screen.turtles()]        
    
if __name__=="__main__":
     
    width,height=600,600
    colors = ["red","orange","yellow","green"]
    
    screen = Screen()
    screen.setup(width,height)
    screen.delay(0)
    screen.bgcolor("black")
    screen.title("旋转的三角形-按空格键跳_作者：李兴球")

    startx = -150
    starty = 150 
    for row in range(4):
        for col in range(4):
            xcor = startx + col * 100
            ycor = starty - row * 100
            Triangle(colors[col],(xcor,ycor))
            
    screen.onclick(reset,3)
    screen.onkey(jump,"space")
    screen.listen()
    screen.mainloop()
