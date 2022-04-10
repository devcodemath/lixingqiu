"""
   顶球重力弹球游戏.py
   本程序主要演示overlap_with命令和角色的polygon与arc命令。
   
   角色的polygon命令以角色自身坐标为第一个点画一个多边形,参数为坐标点列表。
   arc命令用来画饼状图,参数为半径,起始角,结束角。

   角色的overlap_with命令有一个参数，假设为items。
   这个命令会检测items所对应的项目是否和角色的矩形发生重叠，也就是检测是否发生碰撞。
   overlap_with的items参数可能是列表/元组/集合，也可以是另一个角色或一个字符串。
   当items是列表/元组/集合时，则遍历它，检测每个项目是否和角色重叠，返回所重叠的项目集合。
   当items是另一个角色时，取这个角色的项目编号，检测是否和它重叠。
   当items是一个字符串时，认为这是一个标签，遍历所有同一标签的角色，返回所重叠的项目集合。
"""
from sprites import *                   # 从精灵模块导入所有命令   

screen = Screen()                       # 新建屏幕
screen.setup(640,480)                   # 设定宽高
screen.bgcolor('dodger blue')           # 背景颜色

w = Sprite(visible=False)               # 新建隐藏的w角色
x,y = w.topleft()                       # 到左上角
cors = [(x,-y),(x+30,-y),(x+30,y)]
leftborder = w.polygon(cors)            # 以w所在坐标为起点画填充多边形

x,y = w.topright()                      # 到右上角
cors = [(x,-y),(x-30,-y),(x-30,y)]
rightborder = w.polygon(cors)

x,y = w.bottomleft()                     # 到左下角
cors = [(x,y+30),(x+640,y+30),(x+640,y)]
bottomborder = w.polygon(cors)

lrborders = [leftborder,rightborder]     # 左右黑边框
ball = Sprite(1)                         # 新建小球
ball.goto(0,180)                         # 坐标定位
dx = random.randint(-4,4)                # 水平速度
dy = 0                                   # 垂直速度
score = 0                                # 得分
start = time.time()                      # 起始时间
while time.time() - start < 10:          # 当成立的时候    
    x = ball.xcor() + dx
    y = ball.ycor() + dy
    ball.goto(x,y)
    if ball.overlap_with(lrborders):    # 如果碰到左右边框,水平速度取反
        dx = -dx
    if ball.overlap_with(bottomborder): # 如果碰到了下面黑色边框
        dy = -dy                        # y坐标取反
        score -= 3                      # 减三分
    else:                               # 否则
        dy = dy - 0.2                   # dy减小
    if ball.collide_mouse():            # 碰到鼠标指针
        dy = -dy
        score += 5                      # 加5分
    ball.update()                       # 球更新 
    ball.wait(0.01)                     # 等待0.01秒
    screen.title('当前得分：' + str(score))

ball.hide()
ball.goto(0,100)
ball.write2('游戏结束')
ball.addy(-50)
ball.write2('共得分：' + str(score))
screen.mainloop()
