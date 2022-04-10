"""昨夜星辰.py 本程序演示星空中闪烁的星星"""
from turtle import *
from point import *
from random import randint
from winsound import PlaySound,SND_ASYNC,SND_LOOP

class Star(Turtle):
    def __init__(self,images,pos):
        Turtle.__init__(self,visible=False)
        self.penup()                    # 星星不需要画画，所以抬笔
        self.images = images            # 星星的造型列表
        self.index = 0                  # 星星的造型索引初始值
        self.goto(pos.x,pos.y)
        self.twinkle()
        self.st()
        
    def twinkle(self):
        """闪烁方法"""
        self.index = 1 - self.index   # 索引在0和1之间切换
        self.shape(self.images[self.index])
        self.screen.ontimer(self.twinkle,randint(500,1000))

if __name__ == "__main__":

    music = "林淑容-《昨夜星辰》.wav"
    width,height = 800,600
    screen = Screen()
    screen.setup(width,height)
    screen.title("昨夜星辰")
    screen.delay(0)
    screen.bgpic("bg2.png")
    images = ["star1.gif","star2.gif"]
    [screen.addshape(image) for image in images]

    stars_list = []               # 星星列表
    for i in range(50):
        x = randint(-width//2,width//2)
        y = randint(-20,height//2)
        stars_list.append(Point(x,y)) 
            
    while stars_list:
        p = stars_list.pop()
        Star(images,p) 

    PlaySound(music,SND_ASYNC|SND_LOOP)
    screen.exitonclick()
    
    
