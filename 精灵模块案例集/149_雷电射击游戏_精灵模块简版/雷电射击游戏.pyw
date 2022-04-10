"""
   雷电射击游戏_精灵模块简版
   本程序需要Python精灵模块V1.31以上版本支持,   
   本程序的所有敌机是图章,它们可以移动,使用overlap_with进行碰撞检测.....
   作者：李兴球 @ 2020/3/16
"""
from sprites import *                          # 从精灵模块导入所有命令 

enemies_amounts = 200                          # 敌机数量
title = '雷电射击游戏_精灵模块简版'
bgs = ['res/w1.png','res/w2.png','res/w3.png']
exps = ['res/explosion0.png','res/explosion1.png']

screen = Screen()                              # 新建屏幕
screen.setup(960,720)                          # 设定屏幕宽高 
screen.tracer(0,0)                             # 关闭自动刷新和绘画版时
screen.title(title)                            # 设定屏幕所在窗口标题

PlaySound('res/Tragedy Flame.wav',SND_ASYNC|SND_LOOP) # 循环播放背景音乐

index = 0                                      # 定义变量,做为背景表的索引 
def alt_background():
    global index
    screen.bgpic(bgs[index])                   # 设定背景图片
    index = index + 1                          # index增加1 
    index = index % 3                          # index对3求余
    screen.ontimer(alt_background,50)          # 50毫秒后再次运行函数
alt_background()

plane = Sprite(shape='res/敌机1.png',pos=(0,720))
for _ in range(enemies_amounts):               # 这里生成一定数量的敌机 
    x = random.randint(-480,480)
    y = random.randint(720,5440)
    plane.goto(x,y)
    plane.stamp()

bs = Group('zd')                               # 新建子弹组,它们的标签为zd

def shoot():
    if framecounter % 3 == 0 :
        # 下面的bullet角色的标签为zd,它们会自动加入到bs组中
        bullet = Sprite(shape='circle',visible=False,tag='zd')
        bullet.color('yellow')                 # 子弹的颜色
        bullet.scale(0.5)                      # 子弹的缩放
        bullet.goto(player.pos())              # 定位到玩家飞机坐标
        bullet.show()                          # 显示子弹

player = Sprite(shape='res/thunder.png')      # 玩家操作的飞机
player.scale(0.5)
player.sety(-240)                             # 设定玩家飞机的y坐标 

leftkey = Key('a')                            # 新建a键
rightkey = Key('d')                           # 新建d键
upkey = Key('w')                              # 新建w键 
downkey = Key('s')                            # 新建s键
shootkey = Key('j')                           # 新建j键
screen.listen()                               # 监听屏幕

w = Sprite(visible=False)                     # 在屏幕上写分数的角色
w.addy(200)

score = 0                                     # 得分
clock = Clock()                               # 新建时钟对象
framecounter = 0                              # 帧计数器
enemies = plane.stampItems                    # 给plane的图章列表取别名为enemies
while player.isvisible():    
    framecounter += 1                         # 帧计数器加1 
    for item in enemies:                      # 遍历每个图章(敌机)
        plane.movestamp(item,0,-12)           # 向下移动图章(敌机)        
        x,y = plane.stampcors(item)           # 获取敌机坐标
        if y < -360:                          # y小于-360 
            x = random.randint(-480,480)      # 生成一个x
            y = random.randint(720,5440)      # 生成一个y
            plane.stampgoto(item,x,y)         # 把图章移到(x,y)坐标
            plane.stampshow(item)             # 重新显示敌机
    if player.isvisible():                    # 如果玩家飞机可见
        if leftkey.down():player.addx(-5)     # 按a键往左移 
        if rightkey.down():player.addx(5)     # 按d键往右移
        if downkey.down():player.addy(-5)     # 按s键往下移
        if upkey.down():player.addy(5)        # 按w键往上移
        if shootkey.down():shoot()            # 按j键发射子弹
        es = player.overlap_with(enemies)     # 和所有敌机的碰撞检测
        if es:                                # 如果返回非空集合 
            player.hide()                     # 隐藏飞机
            explode(player.pos(),exps)        # 爆炸效果
            [ plane.stamphide(item)  for item in es]
            [ explode(plane.stampcors(item),exps) for item in es]           

    for b in bs:                              # 对于每一颗子弹 
        b.addy(10)                            # 往上移
        if b.ishide():continue
        dead = b.overlap_with(enemies)        # 和每个敌机的碰撞检测
        if dead:
            b.hide()                          # 这颗子弹碰到敌机就隐藏
            for item in dead:                 # 遍历每架碰到子弹的敌机(图章)
               explode(plane.stampcors(item),exps)
               plane.stamphide(item)          # 隐藏这架敌机
               score = score + 10             # 打爆一架得10分
               w.clear()
               info = title + "，当前得分：" +  str(score)
               w.write2(info,font=('',22,'normal'))
    
    # 如果子弹碰到屏幕边缘就删除这颗子弹
    [b.remove() for b in list(bs)[:] if b.collide_edge()]
              
    screen.update()                          # 更新屏幕显示
    clock.tick(60)                           # 设定fps为60

# 玩家所操作的飞机阵亡后显示的一些字
w.clear()
info = "Game Over"
w.write2(info,fg='red',font=('',62,'normal')) # 写阴影字Game Over
w.addy(-200)
info = title + "，当前得分：" +  str(score)
w.write2(info,font=('',22,'normal'))          # 写阴影字,得分情况
screen.mainloop()


