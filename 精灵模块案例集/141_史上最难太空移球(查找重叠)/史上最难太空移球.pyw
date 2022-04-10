"""
   史上最难太空移球.py
   本程序主要体验角色的find_overlapping命令,还有单独的explode命令。
   find_overlapping是用来查找和角色最小矩形重叠的命令，返回这些矩形对应的项目。
   这些项目包括其它角色、所画的线条、填充区域块、图章、dot命令所打的圆点。
   返回一个集合，集合就是找到的项目编号。
   explode是爆炸效果命令，接受一个坐标和一个列表，列表存储的是要显示的一些图片。
"""
from sprites import *                    # 从精灵模块导入所有命令
from random import randint               # 从随机模块导入randint命令

explosionframes = ['res/explosion0.png',
                   'res/explosion1.png']
screen = Screen()                        # 新建屏幕
screen.setup(800,600)                    # 屏幕大小
screen.bgcolor('black')                  # 背景颜色

w = Sprite(visible=False)                # w角色用来画障碍物 
w.color('red')                           # 设定w为红色
w.pensize(50)                            # 画笔粗细为50
w.goto(-300,300)                         # 定位到坐标(-300,300)
w.pendown()                              # 落笔
w.fd(700)                                # 前进700个单位
w.penup()                                # 抬笔
w.goto(-300,-300)                        # 定位到坐标(-300,-300)
w.pendown()                              # 落笔
w.fd(700)                                # 前进700个单位
w.penup()                                # 抬笔
w.pensize(1)                             # 设定画笔粗细为1
w.goto(-300,230)                         # 定位到坐标(-300,230)
# 下面是画6行红色方块,每行有10个
for i in range(6):
    for _ in range(10):
        dy = randint(-20,20)
        w.addy(dy)
        w.draw_rect(35,randint(30,50))   # 画方块,宽度为35,高度为30到50
        w.addy(-dy)
        w.fd(100)                        # 前进100个单位
    w.bk(1000)                           # 倒退1000个单位
    w.addy(-100)                         # 下移100个单位 
      
ball = Sprite(shape=1,pos=(-350,0))      # 这是要操作的主角小球
ball.dx = 0                              # 球的水平速度(这是自定义的属性)
ball.dy = 0                              # 球的垂直速度(这是自定义的属性)

leftkey = Key('Left')                    # 新建左方向箭头 
rightkey = Key('Right')                  # 新建右方向箭头
upkey = Key('Up')                        # 新建上方向箭头
downkey = Key('Down')                    # 新建下方向箭头
screen.listen()                          # 监听键盘按键

result = ""                              # 定义字符串,描述成功还是失败
running = True                           # 定义running变量,控制while是否结束
while running:
    x = ball.xcor() + ball.dx            # 把小球x坐标增加ball.dx
    y = ball.ycor() + ball.dy            # 把小球y坐标增加ball.dy
    ball.goto(x,y)                       # 定位小球到x,y
    if leftkey.down():ball.dx -= 0.1     # 如果按了左方向箭头,则把dx减小0.1
    if rightkey.down():ball.dx += 0.1    # 如果按了右方向箭头,则把dx增加0.1
    if upkey.down():ball.dy += 0.1       # 如果按了上方向箭头,则把dy增加0.1
    if downkey.down():ball.dy -= 0.1     # 如果按了下方向箭头,则把dy减小0.1
    items = ball.find_overlapping()      # 查找有没有和球的矩形进行重叠的项目    
    if items:                            # 如果有项目,则游戏失败!
        running = False
        result = '死亡'
    if ball.xcor() > 350:                # 如果球的x坐标大于350,游戏胜利!
        running = False
        result = '胜利'
    time.sleep(0.01)                     # 等待0.01秒

# 以下根据result的值进行不同的处理
if result == '死亡':                     # 如果result等于'死亡'
    ball.hide()
    ball.play('EXPLO4.wav')              # 播放爆炸声  
    explode(ball.pos(),explosionframes)  # 显示爆炸效果
    w.home()
    w.clear()
    w.write2('失败')                     # 显示'失败'两个字
else:
    ball.play('小号胜利.wav')            # 播放胜利小号声
    w.home()
    w.clear()
    w.write2('胜利!')                    # 显示'胜利'两个字
screen.mainloop()
    
