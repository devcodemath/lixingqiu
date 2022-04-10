"""
   帧动画_纯画笔下雪效果.py
"""
from sprites import *

class Snow:
    def __init__(self,sw,sh):        
        self.sw = sw       # 雪花所在区域的宽度
        self.sh = sh       # 雪花所在区域的高度
        self.dx = 0        # 水平速度
        self.dy = random.uniform(-2,1)
        self.set_pos()

    def set_pos(self):           # 设置坐标 
        self.x = random.uniform(-self.sw//2,self.sw//2)
        self.y = random.uniform(self.sh//2,2 * self.sh)
        
    def move(self):
        self.blow_wind()         # 让鼠标指针的移动影响雪花的水平速度
        self.x += self.dx        # x坐标增加
        self.y += self.dy        # y坐标增加
        self.go_top()            # 如果超边界,则重来 
           
    def pos(self):               # 返回坐标 
        return self.x,self.y

    def go_top(self):
        c1 = self.x > self.sw/2       # 超过最右边界
        c2 = self.x < -self.sw/2      # 超过最左边界
        c3 = self.y < -self.sh//2     # 超过最下边界
        if c1 or c2 or c3: self.set_pos()
           
    def blow_wind(self):
        """向雪花吹吹风"""
        mx,my = mouse_pos()           # 获取鼠标指针坐标
        self.dx = mx/100    

def draw(hg,snow):
    """hg：海龟，snow：雪花点"""
    hg.goto(snow.pos())
    hg.dot(abs(snow.dy)*3)      # 速度越快，雪花点越大

width,height = 480,360
screen = Screen()
screen.tracer(0,0)
screen.bgcolor('black')
screen.setup(width,height)
screen.title("纯画笔下雪效果 Python Sprites Module")

tom = Sprite(visible=False)          # 新建不可见精灵对象
tom.color('white')                   # 颜色为白色

snows = [Snow(width,height) for _ in range(300)]
    
clock = Clock()                       # 新建时钟对象，用来固定fps
while True:
    tom.clear()                       # 清除所有雪花    
    [snow.move() for snow in snows]   # 移动每片雪花 
    [draw(tom,snow) for snow in snows]# 重画每片雪花
    screen.update()                   # 更新显示
    clock.tick(60)
    
        
