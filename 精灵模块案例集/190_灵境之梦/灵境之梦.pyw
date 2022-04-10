"""
   灵境之梦.py   
"""
import time
import random
from sprites import *                           # 从精灵模块导入所有命令

screen = Screen()                               # 新建屏幕 
screen.setup(800,600)                           # 设定宽高 
screen.bgpic('封面.png')                        # 贴上背景
screen.title('灵境之梦__by__李兴球')          # 写上标题

# 显示作品的名字
ti = Sprite(visible=False)
ti.sety(200)
ti.color('white')
ti.write('灵境之梦',align='center',font=('楷体',30,'bold underline'))

# 新建一些角色,每个角色就是一张图片.
ims = [f"素材/{i}.jpg" for i in range(12)]
sps = [Sprite(shape=im) for im in ims]
for i in range(12):
    sps[i].rotatemode(1)
    sps[i].setheading(i*30)

PlaySound('metauni.wav',SND_LOOP|SND_ASYNC)  # 循环播放背景音乐

# 下面是一些图片抖动并散开,最后反弹的代码段
counter = 0
while True:                                  # 让图片擅抖动散开
    pic = sps[counter%12]
    if not pic.collide_edge():               # 如果没有碰到边缘
        pic.fd(random.randint(-4,8))
    counter += 1
    if counter==1100:break
    time.sleep(0.01)
i = 0
while i<10000:                              # 重复10000次
     pic = sps[i%12]
     pic.fd(3)
     pic.bounce_on_edge()                   # 碰到边缘就反弹
     i = i + 1
[sp.hide() for sp in sps]                    # 全部隐藏


# 显示带VR眼睛的男孩图片
feng = Sprite("feng")
for _ in range(6):
    feng.nextshape()
    time.sleep(0.01)

for a in range(255,100,-10):
    feng.setalpha(a)

# 显示一些文字,赋予作品一些内涵
txt = "我是头号编程玩家"
zi = Sprite(visible=False)
zi.goto(-100,180)
zi.color('yellow')
for t in txt:
    zi.write(t)
    zi.fd(30)
    time.sleep(0.1)
zi.goto(0,100)
zi.color('green')
zi.write2('李兴球',align='center',font=('',48,'normal'))

txt = '我做了一个灵境之梦。'
zi.goto(0,50)
zi.color('cyan')
zi.write(txt,align='center',font=('',22,'normal'))
zi.wait(2)

txt = '梦见未来人们都把意识上传到灵境玩去了。'
zi.goto(0,0)
zi.color('white')
zi.write(txt,align='center',font=('',22,'normal'))
zi.wait(3)

txt = '世界全部由人工智能全自动控制。'
zi.goto(0,-50)
zi.color('yellow')
zi.write(txt,align='center',font=('',22,'normal'))
zi.wait(3)

txt = '但是我却是极少数还在真实世界的人类。'
zi.goto(0,-100)
zi.color('pink')
zi.write(txt,align='center',font=('',22,'normal'))
zi.wait(3)

txt = '星河再浩瀚，但我，才是全宇宙的头号玩家！'
zi.goto(0,-150)
zi.color('white')
zi.write(txt,align='center',font=('',22,'normal'))
zi.wait(3)

txt = 'END'
zi.goto(0,-250)
zi.color('light green')
zi.write(txt,align='center',font=('',52,'normal'))

screen.mainloop()


