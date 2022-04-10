"""
   雷电飞行阵列,
   本程序有动态背景,演示一排排敌机从屏幕上方往下移动，直到屏幕最下方。
   这些敌机都是用plane这个角色所盖的图章。
   图章们通过stampItems列表进行管理，它们通过图章的相关命令进行移动。
"""
from sprites import *

bgs = ['res/w1.png','res/w2.png','res/w3.png']

screen = Screen()                       # 新建屏幕
screen.setup(960,720)                   # 设定屏幕宽高 
screen.tracer(0,0)                      # 关闭自动刷新和绘画版时
screen.title('雷电飞行阵列')            # 设定屏幕所在窗口标题

index = 0                               # 定义变量,做为背景表的索引 
def alt_background():
    global index
    screen.bgpic(bgs[index])            # 设定背景图片
    index = index + 1                   # index增加1 
    index = index % 3                   # index对3求余
    screen.ontimer(alt_background,50)   # 50毫秒后再次运行函数
alt_background()

plane = Sprite(shape='res/敌机1.png',pos=(0,720))
for _ in range(200):
    x = random.randint(-480,480)
    y = random.randint(720,5440)
    plane.goto(x,y)
    plane.stamp()                        # 会返回编号，被添加到stampItems列表中 

enemies = plane.stampItems               # 给plane的图章列表取别名 
clock = Clock()
while True:
    for item in enemies:                 # 遍历每个图章(敌机)
        plane.movestamp(item,0,-10)      # 向下移动图章
        x,y = plane.stampcors(item)      # 获取图章坐标
        if y < -360:                     # y小于-360 
            x = random.randint(-480,480) # 生成一个x
            y = random.randint(720,5440) # 生成一个y
            plane.stampgoto(item,x,y)    # 把图章移到(x,y)坐标 
    screen.update()                      # 更新屏幕显示
    clock.tick(60)                       # 设定fps为60
