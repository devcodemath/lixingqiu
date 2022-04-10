""" 打砖块小游戏.py 按方向箭头或用鼠标指针
拖曳拦板去接小球，按回车键开始游戏."""

from turtle import Turtle,Screen
from random import randint,choice
from time import sleep

class Brick(Turtle):
    counter = 0                                   # 类变量，统计消失的砖块数量
    def __init__(self,color,position,balls):
        Turtle.__init__(self,shape='square',visible=False)
        self.penup() 
        self.goto(position)
        self.color(color)                         # 颜色
        self.balls = balls                        # 所有的小球
        self.shapesize(1,2)                       # 变形
        p = self.get_shapepoly()                  # 得到顶点坐标
        self.width = p[1][1] - p[3][1]            # 宽度
        self.height = p[0][0] - p[2][0]           # 高度
        self.left = self.xcor() - self.width//2   # 重定义left
        self.right = self.xcor() + self.width//2  # 重定义right
        self.top = self.ycor() + self.height//2   # 砖块最顶y坐标
        self.bottom = self.ycor() - self.height//2# 砖块最底y坐标
        self.balls_index = 0                      # 所有球的索引号
        self.balls_amounts = len(balls)           # 所有球的数量
        self.st()                                 # 显示
        self.bump_check()
    def bump_check(self):
        """轮换对每个小球进行碰撞检测"""
        if self.isvisible():                      # 如果自己是可见的
            ball = self.balls[self.balls_index]   # 从索引号取一个球
            ball_left = ball.xcor() - 10          # 弹球最左x坐标
            ball_right = ball.xcor() + 10         # 弹球最右x坐标
            ball_top = ball.ycor() + 10           # 弹球最上y坐标
            ball_bottom = ball.ycor() - 10        # 弹球最下y坐标
            c1 = ball_right < self.left  # 弹球最右x坐标小于砖块最左x坐标
            c2 = ball_left > self.right  # 弹球最左x坐标大于砖块最右x坐标
            c3 = ball_top < self.bottom  # 弹球最上y坐标小于砖块最底y坐标
            c4 = ball_bottom  > self.top # 弹球最底y坐标大于砖块最顶y坐标
            separated = c1 or c2 or c3 or c4 # 四个条件有一个成立则碰不到
            if not separated :           # 如果不是分离开的(那就说明碰到了)
                self.ht()                # 隐藏自己
                ball.yspeed = -ball.yspeed # 球的垂直速度取反
                Brick.counter +=1          # 类变量计数器加1
                if Brick.counter == Brick.amounts :    # 数量相等,游戏结束
                   info = "游戏成功结束！"
                   ziti = (None,24,'normal')
                   tmper = Turtle(visible=False)
                   tmper.write(info,align='center',font=ziti)
                   bye_bye = lambda x,y:tmper.screen.bye()
                   tmper.screen.onclick(bye_bye)
            self.balls_index +=1
            self.balls_index = self.balls_index % self.balls_amounts
            self.screen.ontimer(self.bump_check,10)       
    
class Ball(Turtle):    
    def __init__(self):
        Turtle.__init__(self,shape='circle')
        self.penup()                                    # 抬笔
        self.color("red")                               # 颜色
        speedlist = [-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]
        self.xspeed = choice(speedlist)                 # 水平速度
        self.yspeed = choice(speedlist)                 # 垂直速度
        self.sw = self.screen.window_width()  # 屏幕宽度
        self.sh = self.screen.window_height()# 屏幕高度

    def move(self,board):
        x = self.xcor() + self.xspeed     # 水平方向移动self.xspeed
        y = self.ycor() + self.yspeed     # 垂直方向移动self.yspeed
        self.goto(x,y)        
        if abs(x) > self.sw//2 : self.xspeed = -self.xspeed
        if y > self.sh//2: self.yspeed = -self.yspeed        
        if y < -self.sh//2: self.ht()      # 超过下边界就隐藏
        if self.bump(board): self.yspeed = -self.yspeed # 碰到拦板y速度反向

    def bump(self,board):
        x = self.xcor()            # 球中心点的x坐标
        y = self.ycor() - 10       # 球的半径是10,
        left = board.xcor() - 100  # 拦板最左边x坐标(板子的长度是200)
        right = board.xcor() + 100 # 拦板最右边x坐标
        top = board.ycor()  + 10   # 拦板最顶y坐标
        bottom = board.ycor() - 10 # 拦板最顶y坐标
        return x < right and x > left and y < top and y > bottom
    
def start(screen,writer ):
    """生成拦板,绑定按键,小球和砖块,让小球不断移动。"""
    writer.clear()                       # 按回车键后清除所写的标题
    screen.onkeypress(None,"Return")     # 取消回车键事件绑定
    screen.bgcolor("white")              # 重设背景色为白
    height = screen.window_height()      # 得到屏幕高度
    board  = Turtle(shape = 'square')    # 新建形状为square的方形体
    board.shapesize(1,10)                # 长方形的长度为200x20像素     
    board.penup()                        # 抬笔
    board.color("blue")                  # 设颜色
    board.sety(50-height/2)              # 把拦板y坐标定位
    def move_to_right():
        board.setx(board.xcor() + 10)    # x坐标右移10个单位        
    def move_to_left():
        board.setx(board.xcor() - 10)    # x坐标左移10个单位        
    
    screen.onkeypress(move_to_right,"Right")# 绑定右方向箭头
    screen.onkeypress(move_to_left,"Left")  # 绑定左方向箭头
    board.ondrag(lambda x,y:board.setx(x))  # 绑定拖动事件

    all_balls = [Ball() for i in range(2)]  # 生成两个球
    rows  = 4
    cols = 6
    Brick.amounts = rows * cols             # 类变量，用来代表砖块所有数量
    startpos = (-120,160)                   # 所有砖块的起点坐标
    for r in range(rows):                   # 一行一行的排砖块
        for c in range(cols):               # 一行之中的每一块砖
            x = startpos[0] + c * 50        # 设定x坐标
            y = startpos[1] - r * 40        # 设定y坐标
            Brick('magenta',(x,y),all_balls)# 生成砖块   
    while True:
        for ball in all_balls:
            if ball.isvisible():ball.move(board)
            screen.update()
            sleep(0.01)
            
def main():
    """新建屏幕,显示标题,按回车键开始游戏"""
    title = "打砖块小游戏"
    width,height = 480,360
    screen = Screen()                        # 新建屏幕
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

 
  
