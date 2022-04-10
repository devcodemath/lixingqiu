"""飘移粒子效果.py，本程序新建Particle类。
当鼠标指针左右移动的时候粒子的运动方向也会改变。
下一个升级版本:白桦林的故事,Python多媒体配音MV,个人博客:
www.lixingqiu.com
"""

__author__ = "李兴球"
__date__   = "2019/1/29"
from turtle import Turtle,Screen
from random import randint,choice
 

class Particle(Turtle):
    shift = 1           # 类变量,它的值由鼠标的相对移动而改变
    def __init__(self,c):        
        Turtle.__init__(self,shape='dot',visible=False)
        self.penup()        
        self.color(c)
        self.aspeed = -0.5
        self.sh = self.screen.window_height()      # 屏幕高度
        self.init()
        
    def init(self):
        self.ht()                                  # 隐藏自己
        self.goto(0,100)                           # 坐标定位
        self.xspeed = randint(1,5) * Particle.shift# 横向速度
        self.yspeed = randint(5,10)                # 垂直速度
        self.st()                                  # 显示自己
        
    def move(self):
        """根据x和y速度移动"""
        x = self.xcor() + self.xspeed   # 水平坐标增加横向速度
        y = self.ycor() + self.yspeed   # 垂直坐标增加垂直速度   
        self.goto(x,y)         
        if y < -self.sh//2 :            # 到屏幕最低就重新init
            self.init()
        else:
            self.yspeed = self.yspeed + self.aspeed #加速度下落
            
def wind(event):
    global oldx
    Particle.shift = event.x - oldx    # 鼠标x坐标相对移动    
    oldx = event.x                     # 记录鼠标指针坐标
    
if __name__ == "__main__":

    oldx = 0                           # 记录上次的鼠标x坐标
    counter = 0                        # 计数器变量
    amounts = 150                      # 设定粒子总数
    color_list = ['white','white','white','white','red','orange']
    color_list.extend(['yellow','green','cyan','blue','purple'])
    color_list.extend(['pink','brown','magenta','gray','white'])
    width,height = 480,360
  
    screen = Screen()                   #  新建屏幕
    screen.addshape("dot",((0,0),(0,0)))# 设定dot形状
    screen.setup(width,height)          # 设定屏幕宽高
    screen.bgcolor("black")             # 设定屏幕背景
    screen.bgpic("bg.png")              # 设定背景图片
    screen.title("飘移粒子效果_风火轮少儿编程") # 设定屏幕标题   
    screen.delay(0)                     # 设定屏幕延时
    screen.cv.bind("<Motion>",wind)     # 绑定移动事件
    ps = []                             # 定义粒子列表
    while True:                         # 进入无限循环
        if counter < amounts:           # 未达指定数量
           p = Particle(choice(color_list)) # 生成粒子
           ps.append(p)                 # 添加到列表
           counter += 1                 # 计数器加一
        for p in ps:                    # 迭代每个粒子
            p.move()                    # 移动这个粒子
        screen.update()                 # 屏幕刷新重画
    "本人制作了大量基于pygame和turtle的创意编程作品,有需要订制可和我联系"
        

    
