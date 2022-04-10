"""
   AI自动打砖块游戏,
   屏幕由画布和水平滚动条及垂直滚动条组成。
   屏幕上所有项目其实都有一个编号。可以用屏幕的cv属性获取画布对象。
   画布有相关方法可以对它上面的项目进行操作，如删除一个项目甚至移动一个项目。
   本课主要学习的内容是从总体上理解程序即可。
"""
import math                                     # 导入数学模块
from sprites import *                           # 从精灵模块导入所有命令

PlaySound('背景音乐.wav',SND_ASYNC|SND_LOOP)    # 播放背景音乐
width,height = 800,600                          # 定义屏幕宽高变量
screen = Screen()
screen.setup(width,height)                      # 设定屏幕宽高
screen.bgpic('800x600.png')                     # 设定背景图片  
screen.title('AI自动打砖块游戏by李兴球www.lixingqiu.com')                # 设定标题

board = Sprite(shape='square')                  # 这做为拦板
board.color('red','cyan')                       # 拦板的边框和填充颜色
board.shapesize(0.5,5,3)                        # 缩放拦板 
board.speed(1)                                  # 拦板移动速度为1
board.goto(0,-200)                              # 拦板初始坐标定位

ball = Sprite(1)                                # 新建小球角色
ball.setheading(-45)                            # 面向-45度方向

brick = Sprite(visible=False)                   # 新建砖块角色
brick.color('red','brown')                      # 砖块的颜色
rect = -width/2,width/2,50,250                  # 砖块随机移动的矩形范围 
bricks = []                                     # 所有砖块项目表
compute = True                                  # 决定是否要计算拦板x坐标的逻辑变量
while True:
    ball.fd(10)
    if ball.overlap_with(board):                # 如果碰到拦板
        ball.setheading(-ball.heading())        # 反弹方向
    ball.bounce_on_edge()                       # 碰到边缘就反弹
    
    if random.randint(1,50)==1:                 # 以一定的机率产生砖块
        brick.gotorandom(*rect)                 # 到随机位置
        x,y = brick.pos()
        cors = [(x+50,y),(x+50,y+10),(x,y+10)]  # 设定多边形其余3个坐标点
        bricks.append(brick.polygon(cors))      # 生成砖块，加到砖块表
        
    items = ball.overlap_with(bricks)           # 检测球和砖块们的碰撞
    if items:ball.setheading(-ball.heading())   # 如果碰到了,球就反弹
    for item in items:                          # 对于碰到了的砖块项目
        bricks.remove(item)                     # 从砖块列表中移除
        screen.cv.delete(item)                  # 从画布上移除
    # 下面是当球的y坐标小于0，并且方向为向下时，计算拦板的x坐标    
    fx = ball.heading()                         # 球的方向
    if ball.ycor() < 0 and fx < 360 and fx > 180 and compute== True:
        bx = 200/math.tan(math.radians(-fx))
        x  = bx+ball.xcor()
        if abs(x)<400:
           board.goto(bx+ball.xcor(),board.ycor())
           compute = False
    if ball.ycor()>=0 : compute=True
    screen.update()
    time.sleep(0.01)
