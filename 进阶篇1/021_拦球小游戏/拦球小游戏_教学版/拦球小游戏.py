""" 拦球小游戏.py 按方向箭头或用鼠标指针拖曳拦板去接小球。按回车键开始游戏."""

from turtle import Turtle,Screen
from random import randint,choice
from time import sleep
 
class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self,shape='circle')
        self.penup()                                # 抬笔
        self.color("red")                           # 颜色
        speedlist = [-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]
        self.xspeed = choice(speedlist)             # 水平速度
        self.yspeed = choice(speedlist)             # 垂直速度
        self.sw = self.screen.window_width()        # 屏幕宽度
        self.sh = self.screen.window_height()       # 屏幕高度

    def move(self,board):
        x = self.xcor() + self.xspeed     # 水平方向移动self.xspeed
        y = self.ycor() + self.yspeed     # 垂直方向移动self.yspeed
        self.goto(x,y)        
        if abs(x) > self.sw//2 : self.xspeed = -self.xspeed
        if abs(y) > self.sh//2: self.yspeed = -self.yspeed
        if self.bump(board): self.yspeed = -self.yspeed # 碰到拦板垂直速度反向

    def bump(self,board):
        x = self.xcor()            # 球中心点的x坐标
        y = self.ycor() - 10       # 球的半径是10,
        left = board.xcor() - 100  # 拦板最左边x坐标(板子的长度是200)
        right = board.xcor() + 100 # 拦板最右边x坐标
        top = board.ycor()  + 10   # 拦板最顶y坐标
        bottom = board.ycor() - 10 # 拦板最顶y坐标
        condition = x < right and x > left and y < top and y > bottom
        return condition
    
def start(screen,writer ):
    """生成拦板,绑定按键,小球移动"""
    writer.clear()                       # 按回车键后清除所写的标题
    screen.onkeypress(None,"Return")     # 取消回车键事件绑定
    screen.bgcolor("white")
    height = screen.window_height()
    board  = Turtle(shape = 'square')    # 通过 board.get_shapepoly()可得到顶点坐标，从而得长宽
    board.shapesize(1,10)                # 长方形的长度为200x20像素     
    board.penup()                        # 抬笔
    board.color("blue")                  # 设颜色
    board.sety(50-height/2)              # 把拦板y坐标定位
    def move_to_right():
        board.setx(board.xcor() + 10)    # x坐标右移10个单位        
    def move_to_left():
        board.setx(board.xcor() - 10)    # x坐标左移10个单位        
    
    screen.onkeypress(move_to_right,"Right") # 绑定右方向箭头
    screen.onkeypress(move_to_left,"Left")   # 绑定左方向箭头
    board.ondrag(lambda x,y:board.setx(x))   # 绑定拖动事件

    all_balls = [Ball() for i in range(3)]   # 生成三个球

    while True:
        for ball in all_balls:
            ball.move(board)
            sleep(0.001)
            
def main():
    """新建屏幕,显示标题,按回车键开始游戏"""
    title = "拦球小游戏"
    width,height = 480,360
    screen = Screen()                         # 新建屏幕
    screen.delay(0)                          # 延时为0
    screen.bgcolor("black")                  # 背景为黑
    screen.title(title)                      # 标题为title
    screen.setup(width,height)
    
    w = Turtle(visible=False)                # 用来写标题的海龟
    w.color("cyan")                          # 颜色为青色
    w.penup()                                # 抬笔
    w.write(title,align='center',font=("楷体",32,"normal"))
    w.sety(-100)                             # 下移100个单位
    w.color("gray")                          # 颜色为灰色
    w.write("按回车键开始",align='center',font=("黑体",12,"normal"))   

    screen.onkeypress(lambda:start(screen,w),"Return") # 绑定回车到匿名函数
    screen.listen()                          # 监听屏幕(设置焦点) 
    screen.mainloop()                        # 进入主循环
    
if __name__ == "__main__":

    main()

 
  
