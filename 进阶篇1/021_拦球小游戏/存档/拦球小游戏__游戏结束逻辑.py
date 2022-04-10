""" 
   需要讲类变量.
   
"""

from turtle import Turtle,Screen
from random import randint
from time import sleep
 
class Ball(Turtle):
    
    counter = 0
    def __init__(self):
        Turtle.__init__(self,shape='circle')
        self.penup()
        self.color("cyan")
        self.xspeed = randint(-6,6)
        self.yspeed = randint(-6,6)
        self.screen_width = self.screen.window_width()
        self.screen_height = self.screen.window_height()
        Ball.counter = Ball.counter + 1                    #生成了下则计个数        
        self.dead = False
    def move(self,board):
        if not self.dead:
            x = self.xcor() + self.xspeed
            y = self.ycor() + self.yspeed
            self.goto(x,y)        
            if abs(x) > self.screen_width//2 : self.xspeed = -self.xspeed
            
            if y > self.screen_height//2: self.yspeed = -self.yspeed

            if y < -self.screen_height//2:
                self.dead = True 
                Ball.counter = Ball.counter - 1
                self.screen.title(str(Ball.counter))           
            
            if self.bump(board): self.yspeed = -self.yspeed
     

    def bump(self,board):
        x = self.xcor()
        y = self.ycor() - 10       #球的半径是10,
        left = board.xcor() - 100
        right = board.xcor() + 100
        top = board.ycor()  + 10
        bottom = board.ycor() - 10
        condition = x < right and x > left and y < top and y > bottom
        return condition
    
def start(screen,writer ):
    writer.clear()
    screen.onkeypress(None,"Return")
    height = screen.window_height()
    board  = Turtle(shape = 'square')    # 通过 board.get_shapepoly() 可得到顶点坐标，从而得长宽
    board.shapesize(1,10)                # 长方形的长度为200x20像素
    print(board.get_shapepoly())
    board.penup()                        # 抬笔
    board.color("yellow")                  # 设颜色
    board.sety(50-height/2)              # 把拦板y坐标定位

    def move_to_right():
        board.setx(board.xcor() + 10)    # x坐标右移10个单位
        
    def move_to_left():
        board.setx(board.xcor() - 10)    # x坐标左移10个单位        
    
    screen.onkeypress(move_to_right,"Right")
    screen.onkeypress(move_to_left,"Left")

    all_balls = [Ball() for i in range(3)]

    running = True
    while running:
        for ball in all_balls:
            ball.move(board)
            if Ball.counter == 0 : 
                running = False
                break
        sleep(0.0001)
    writer.sety(100)
    writer.write("游戏结束",align='center',font=("宋体",32,"normal"))
    
            
def main():

    title = "拦球小游戏"
    width,height = 800,600
    screen = Screen()
    screen.delay(0)
    screen.bgcolor("black")
    screen.title(title)
    
    w = Turtle(visible=False)
    w.color("cyan")
    w.penup()    
    w.write(title,align='center',font=("楷体",32,"normal"))
    w.sety(-100)
    w.color("gray")
    w.write("按回车键开始游戏",align='center',font=("黑体",12,"normal"))   

    screen.onkeypress(lambda:start(screen,w),"Return")
    screen.listen()

    
if __name__ == "__main__":

    main()

 
  
