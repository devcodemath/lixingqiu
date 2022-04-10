""" ball.py。 本程序新建Ball类,它继承自Turtle。"""
from glob import glob
from turtle import Screen,Turtle
from random import randint,choice
from board import Board
from time import sleep

class Ball(Turtle):
    def __init__(self,image,board ):
        """image:已注册的gif图"""
        Turtle.__init__(self,shape=image,visible=False)
        self.penup()
        self.board = board
        self.xspeed = choice(speeds)
        self.yspeed = choice(speeds)
        self.screen_width = self.screen.window_width()  # 屏幕宽度属性
        self.screen_height = self.screen.window_height()# 屏幕高度属性
 
        self.dead = False
 
        self.goto(self.screen_width//2,self.screen_height//2)
        self.showturtle()
        self.move()
    def move(self):
        """移动小球方法"""        
        if self.dead == False:
            x = self.xcor() + self.xspeed        # 新的x坐标是原坐标加xspeed
            y = self.ycor() + self.yspeed        # 新的y坐标是原坐标加yspeed
            self.goto(x,y)
            left = x - 13                        # 小球最左边的x坐标
            right = x + 13                       # 小球最右边的x坐标
            top = y-13                           # 小球最上边的y坐标
            bottom = y + 13                      # 小球最下边的y坐标
            c1 = left <= 0
            c2 = right >= self.screen_width
            if c1 or c2 :                        # 左或右超过边缘
                self.xspeed = -self.xspeed       # x速度取反
                
            c3 = top <= 0
            c4 = top >= self.screen_height
            if c3 :                              # 超过上边缘
                self.yspeed = -self.yspeed       # y速度取反
            if c4 :                              # 超过下边缘
                self.dead = True                 # 死了
                self.ht()                        # 隐藏
            if self.is_bumped_board():
                 self.yspeed = -self.yspeed       # y速度取反
            self.screen.ontimer(self.move,10)
        
    def is_bumped_board(self):
        x = self.xcor()         # 新的x坐标是原坐标加xspeed
        y = self.ycor()         # 新的y坐标是原坐标加yspeed
        ball_top = y-13                           # 小球最上边的y坐标
        ball_bottom = y + 13                      # 小球最下边的y坐标
        board_left = self.board.xcor() - 100
        board_right = self.board.xcor() + 100
        board_top = self.board.ycor() - 15
        board_bottom = self.board.ycor() + 15
        c1 = x > board_left
        c2 = x < board_right
        c3 = ball_bottom > board_top
        c4 = ball_bottom < board_bottom
        return c1 and c2 and c3 and c4
        
                
  
            
        
        
if __name__ == "__main__":

    wood_image = "wood.gif"
    width,height = 800,600
    game_title= "接彩球游戏"
    gif_images = glob("images/*.gif")
    speeds = [x for x in range(-6,6) if x!=0] # 如果x不是0则加到列表中

    screen = Screen()
    screen.delay(0)                           # 屏幕延时为0毫秒
    screen.bgcolor("black")                   # 设定屏幕背景色
    screen.setup(width,height)                # 设定屏幕宽高
    screen.setworldcoordinates(0,height,width,0)         # 进行坐标转换
    screen.cv.master.resizable(width=False,height=False) # 固定窗口大小
    screen.title("Ball类演示程序")
    [screen.addshape(image) for image in gif_images] # 注册所有gif到屏幕
    screen.addshape(wood_image)

    board = Board(wood_image)
    
    amounts = 5
    balls = [Ball(choice(gif_images),board) for i in range(amounts)]
    running = True
    def setclose(x,y):
        global running                         # 申明为全局变量
        running = False
    screen.onclick(setclose)                   # 单击屏幕关窗口
    index = 0
    
 
 
                                    
    screen.mainloop()                               # 关闭窗口
 

