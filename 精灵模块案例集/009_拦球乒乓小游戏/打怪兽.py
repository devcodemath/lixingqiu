"""
   拦球小游戏.py,本程序主要演示的是如何获取鼠标指针的坐标,
   还有碰撞检测命令,以及Clock类如何使用。
   本程序需要Python精灵模块支持,安装最新版本请用如下命令。
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites    --upgrade
   技术支持：李兴球。QQ：406273900
"""

from sprites import *          # 从精灵模块导入所有命令

ball = Sprite(visible=False)               # 新建小怪
ball.ht()
ball.randomheading()           # 设定随机方向
ball.screen.bgcolor("dodger blue") # 设定背景颜色

# 新建矩形(拦板)
board = Sprite(shape='square',pos=(0,-250))
board.color("brown",'gold')
board.shapesize(0.5,5,2)       # 矩形变形为长条

zd = Sprite(1)
zd.scale(0.5)
zd.ht()
zd.left(90)

clock = Clock()                # 新建时钟对象
leftkey = Mouse()              # 新建鼠标左键
counter = 1000
while True:
    counter += 1
    if zd.isvisible():
        zd.fd(10)
        if zd.collide_edge():zd.ht()
    
    if leftkey.down() and zd.ishide():         # 如果单击了鼠标左键,则发射
        zd.goto(board.pos())
        zd.show()
    if counter>=1000 and ball.ishide():ball.show()
    if ball.isvisible():ball.fd(10)                # 前进10
    if ball.collide(zd) and zd.isvisible():
        ball.ht()
        explode(ball,['res/explosion0.png','res/explosion1.png'])
        counter = 0
    ball.bounce_on_edge()      # 碰到边缘就反弹

    mx,my = mouse_pos()        # 获取鼠标指针坐标
    board.setx(mx)             # 把矩形的x坐标设为鼠标指针的x坐标
  
    if ball.collide(board) :   # 如果碰到拦板
      ball.setheading(-ball.heading())  # 或直接向后转,ball.right(180)
    clock.tick(60)             # 固定fps为60  

