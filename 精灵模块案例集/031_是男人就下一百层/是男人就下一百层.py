"""
   是男人就下一百层雏形，这个游戏没有继续完善下去。
   只是提供最简单的代码，方便学习。
"""
from sprites import *

class Wood(Sprite):
    """继承自Sprite的Wood类，用来生成木条"""
    def __init__(self,shape='square',visible=False):
        Sprite.__init__(self,shape=shape,visible=visible)
        self.sw = self.screen.window_width()   # 窗口宽度
        self.sh = self.screen.window_height()  # 窗口高度
        self.isdanger = random.choice([True,False,False])
        if self.isdanger:              # 如果是危险的则为红色
            self.color('gray','red')
        else:
            self.color('gray','green')       
        self.init()
        
    def init(self):
        self.hide()
        self.shapesize(1,random.randint(5,10),4)
        x = random.randint(-self.sw//2,self.sw//2)
        y = random.randint(-3 * self.sh,-self.sh//2 )
        self.goto(x,y)
        self.show()        

    def update(self):
        self.move(0,5)
        if self.ycor() > self.sh//2 + 20:
            self.init()

akey = Key('a')         # a键实例,注意不是A
dkey = Key('d')         # d键实例,按了大写D无法移动

screen = Screen()       # 新建屏幕
screen.setup(480,780)   # 设定屏幕分辨率
screen.bgcolor('black') # 设定屏幕背景为黑
screen.title("是男人就下一百层原理程序")

man = Sprite('man.png') # 只是个dummy
man.rotatemode(1)       # 左右翻转

# 人会移到脚的坐标靠上一定的距离
foot = Sprite(shape='square',pos=(0,200) )
foot.dy = -5
foot.da = -0.5                       # 加速度
foot.shapesize(0.3,1.5)              # 缩放大小

ws = [ Wood() for x in range(10)]    # 设10根
currentwood = ws[0]
screen.listen()                      # 监听按键 
clock = Clock()                      # 新建时钟对象
while 1:
    [w.update() for w in ws]        # 每根都移动
    if akey.down():                 # 按a键往左移
        foot.addx(-5)               # 左移5个单位
        man.setheading(180)         # 朝向左的方向
    if dkey.down():                 # 按d键往右移 
        foot.addx(5)                # 右移5个单位
        man.setheading(0)           # 朝向右的方向
        
    foot.addy(foot.dy)             # 往下掉
    x,y = foot.pos()               # 获取脚的坐标
    man.goto(x,y+50)               # 人移到脚的位置

    # 没有碰到则加速度下落
    if not foot.collide(currentwood):
        foot.dy = foot.dy + foot.da # 加速往下掉
    for w in ws:                    # 每根木条 
        if foot.collide(w):         # 如果脚碰撞到了木条
            foot.dy = 5             # 和木条一样的y速度了
            foot.sety(w.ycor()+5)   # 站在木条上
            currentwood = w
            foot.da = 0           # 向下的加速度为0 
            break
    if not foot.collide(currentwood):
        foot.da = -0.5 
    
    screen.update()
    clock.tick(60)
