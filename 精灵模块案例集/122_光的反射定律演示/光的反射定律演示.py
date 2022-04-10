"""
   光的反射定律演示,本课了解一下默认的多边形造型列表,
   通过screen.getshapes()可得到这个列表,
   还要学习一下shapesize命令的用法,
   它让角色的造型发生变形,但并不支持图形角色。
"""
from sprites import *

def make_photon():
    """在坐标(-50,0)生成一粒光子"""
    photon = Sprite(shape='dot',pos=(-50,0))
    photon.randomcolor()                # 随机颜色
    photon.dx = 2                       # 水平速度
    photon.dy = -4                      # 垂直速度
    ps.append(photon)                   # 加到列表
    
screen = Screen()                       # 新建屏幕 
screen.bgcolor('black')                 # 涂背景色
screen.setup(480,360)                   # 设定宽高  
screen.tracer(0,0)                      # 关闭自动刷新 

ps = []                                 # 新建列表
# 新建一块方形的反射板,坐标为(0,-103)
board = Sprite(shape='square',pos=(0,-103))
board.color('cyan')                     # 反射板 
board.left(90)                          # 左转90度
board.shapesize(10,0.1)                 # 宽高变形  

s = '光的反射定律演示'
ft = ('黑体',16,'normal')               # 定义三元组
w = Sprite(visible=False)               # 生成隐藏的w角色 
w.goto(0,100)                           # 定位到坐标(0,100)
w.color('white')                        # 设定颜色为白
w.write(s,align='center',font=ft)       # 写标题   
w.color('gray')                         # 设定颜色为灰
w.addy(-20)                             # 往下移20个单位
w.pendown()                             # 落笔
w.goto(0,-100)                          # 定位到(0,-100) 

while True:
    if len(ps)<100:                     # 如果还没有100个光子
        make_photon()                   # 生成一粒光子 
    for p in ps:                        # 每一颗光子 
        x = p.xcor() + p.dx             # 设定x坐标     
        y = p.ycor() + p.dy             # 设定y坐标
        p.goto(x,y)                     # 定位到(x,y)
        if p.ycor()<=-100:p.dy = -p.dy  # 如果y坐标小于-100则y速度取反
        if p.collide_edge():            # 如果碰到边缘
            p.hide()                    # 隐藏
            p.goto(-50,0)               # 定位到(-50,0)坐标
            p.dy = -4                   # 垂直速度为-4
            p.show()                    # 显示
    screen.update()                     # 更新屏幕显示
    time.sleep(0.1)                     # 等待0.1秒 
    
    
