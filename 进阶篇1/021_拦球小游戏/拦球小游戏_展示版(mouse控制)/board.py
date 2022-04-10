"""board.py 本程序新建board类"""

from turtle import *

class Board(Turtle):
    def __init__(self,image):
        Turtle.__init__(self,shape=image,visible=False)
        self.penup()
        self.speed(0)
        self.screen_width = self.screen.window_width()   # 屏幕宽度
        self.screen_height = self.screen.window_height() # 屏幕高度
        self.screen.cv.bind("<Motion>",self.follow_mouse)# 绑定鼠标移动事件
        self.goto(0,self.screen_height - 50)             # 初始定位
        self.showturtle()                                # 显示
        
    def follow_mouse(self,event):
        """跟随鼠标事件函数"""
        self.setx(event.x)


if __name__ == "__main__":        
        
    wood_image = "wood.gif"
    width,height = 800,600
    game_title= "接彩球游戏"
    
    screen = Screen()
    screen.setup(width,height)    
    screen.setworldcoordinates(0,height,width,0)         # 进行坐标转换
    screen.delay(0)
    screen.title(game_title)
    
    screen.addshape(wood_image)
    screen.cv.master.resizable(width=False,height=False) # 固定窗口大小
    board = Board(wood_image)
    screen.mainloop()
