"""
   换桶接方块游戏.py
   操作方法，单击屏幕，交换颜色桶的位置，让方块落入相应颜色的桶中，
   如果落入同样颜色桶中，则加10分，否则生命数减一。
   随着方块的移动速度越快，游戏难度会越来越大！
   本程序由于配音的需要，借用了pygame的混音器，所以也要安装pygame模块，
   安装方法pip install pygame
   python精灵模块安装方法： pip install sprites
"""
from sprites import *
from pygame import mixer

def swapbuck(index1,index2):
    """交换桶的位置"""
    # 以下是交换桶的坐标
    x1,y1 = bucks[index1].pos()
    x2,y2 = bucks[index2].pos()
    bucks[index1].goto(x2,y2)
    bucks[index2].goto(x1,y1)
    # 以下是交换列表中‘桶’的索引位置
    bucks[index1],bucks[index2] = bucks[index2],bucks[index1]
    while  leftkey.down():screen.update()
    
def makesquare():
    """随机产生一个方块"""
    r = random.randint(1,4)
    if r == 1:
       sq = Sprite('res/redfk.png',tag='red',pos=(random.choice(xcors),180))
    elif r == 2:
        sq = Sprite('res/yellowfk.png',tag='yellow',pos=(random.choice(xcors),180))
    elif r == 3:
        sq = Sprite('res/greenfk.png',tag='green',pos=(random.choice(xcors),180))
    elif r == 4:
        sq = Sprite('res/bluefk.png',tag='blue',pos=(random.choice(xcors),180))        
    squares.append(sq)
    
def removesquare():
    """移去到底的方块
       遍历每个方块，如果到桶上了，则判断到了哪个桶上，
       然后判断它们的标签是否相等，如果相等，则加10分，否则爆炸！
    """
    global score,lives,speed                              # 得分和生命数与速度为全局变量 
    for sq in squares[:]:
        if sq.ycor() < -100:
            item = sq.find_overlapping()                  # 查找方块碰到的所有item
            item = list(item)[0]                          # 这里只有一个，所以取索引为0的
            if sq.get_tag() == buckitems[item]. get_tag():# 如果这个方块的标签和桶的标签相等
                score = score + 10
                if score % 100 == 0 : speed = speed + 0.5 # 超过百分则速度加0.5，游戏难度加大# 则加10分
                screen.title('得分' + str(score) + ",生命数：" + str(lives))
                effect(sq.pos(),'res/success.png')        # 显示打勾的一张图片！
                random.choice( snd_success).play()        # 播放成功音效
            else:
                explode(sq.pos(),'res/explode.png')       # 这是最简单的爆炸效果！
                lives -= 1                                # 生命数减去一
                screen.title('得分' + str(score) + ",生命数：" + str(lives))
                snd_explode.play()                        # 播放失败音效
               
            squares.remove(sq)                            # 从squares列表中移除这个方块
            sq.remove()                                   # 从画布上移除这个项目

mixer.init()                                              # 初始化混音器
success1 = mixer.Sound('res/success1.wav')                # 成功1音效
success2 = mixer.Sound('res/success2.wav')                # 成功1音效
success3 = mixer.Sound('res/success3.wav')                # 成功1音效
success4 = mixer.Sound('res/success4.wav')                # 成功1音效
snd_success = [success1,success2,success3,success4]       # 放入列表以便随机选取
snd_explode = mixer.Sound('res/explode.wav')              # 爆炸音效   

screen = Screen()
screen.setup(480,360)
screen.bgcolor('#393837')
screen.title('换桶接方块游戏')
screen.bgpic('res/cover.png')                            # 显示封面
spacekey = Key('space')                                  # 空格按键
screen.listen()                                          # 监听屏幕按键
PlaySound('res/menu.wav',SND_LOOP|SND_ASYNC)             # 循环播放背景音乐
while not spacekey.down():screen.update()                # 等待空格键被按下
screen.bgpic('nopic')                                    # 取消封面

PlaySound('',SND_PURGE)                                  # 停止播放声音  
PlaySound('res/game.wav',SND_LOOP|SND_ASYNC)             # 循环播放背景音乐
xcors = [-168,-56,56,168]
shapes = ['res/redfk.png','res/yellowfk.png',
          'res/greenfk.png','res/bluefk.png',
          'res/explode.png','res/success.png']

redbuck = Sprite('res/red.png',pos=(-168,-130),tag='red')
yellowbuck = Sprite('res/yellow.png',pos=(-56,-130),tag='yellow')
greenbuck = Sprite('res/green.png',pos=(56,-130),tag='green')
bluebuck = Sprite('res/blue.png',pos=(168,-130),tag='blue')

# 项目编号和角色的映射
buckitems = {redbuck.turtle._item:redbuck,
         yellowbuck.turtle._item:yellowbuck,
         greenbuck.turtle._item:greenbuck,
         bluebuck.turtle._item:bluebuck}
bucks = [redbuck,yellowbuck,greenbuck,bluebuck]

swap = Sprite('res/swap-arrow.png',pos=(0,-50)) # 交换指示杠
leftkey = Mouse()                               # 鼠标左键
squares = []                                    # 所有方块列表
clock = Clock()                                 # 时钟对象
score = 0                                       # 得分
lives = 3                                       # 生命数
speed = 2                                       # 下移速度 
while lives > 0:    
    mx,my = mouse_pos()
    if mx<60 and mx > -60:
        swap.setx(0)
        if leftkey.down():swapbuck(1,2)
    elif mx <-60 and mx > -180:
        swap.setx(-120)
        if leftkey.down():swapbuck(0,1)
    elif mx < 180 and mx > 60:
        swap.setx(120)
        if leftkey.down():swapbuck(2,3)

    if random.randint(1,100)==1 and len(squares) < 1:
        makesquare()
    [sq.addy(-speed) for sq in squares]
    removesquare()                            # 移去方块    
    screen.update()                           # 屏幕刷新
    clock.tick(60)                            # 固定fps为60
    
swap.hide()                                   # 隐藏交换指示杠
[buck.hide() for buck in bucks]               # 隐藏每只桶
screen.bgpic('res/gameover.png')              # 显示新的背景
PlaySound('',SND_PURGE)                       # 停止播放声音  
PlaySound('res/gameover.wav',SND_LOOP|SND_ASYNC)
screen.mainloop()
