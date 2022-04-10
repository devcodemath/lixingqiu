"""
   飞扬小鸟Python精灵模块简版
"""

from sprites import *

width,height = 480,360
bimages = [f'res/costume{i}.png' for i in range(1,5)]

screen = Screen()
screen.setup(width,height)
screen.bgpic('res/背景.png')
screen.title('飞扬小鸟Python精灵模块简版')

leftkey = Mouse(1)                         # 左键

# 循环播放背景音乐
s = Sprite(visible=False).play('res/音乐.wav',loop=True)

dummy = Sprite(visible=False)
dummy.addy(100)
dummy.write("飞扬小鸟Python精灵模块简版",align='center',font=('楷体',22,'normal'))
dummy.addy(-80)
dummy.write("writed by lixingqiu",align='center',font=('黑体',18,'bold'))
dummy.addy(-100)
dummy.write("click to start the game",align='center',font=('宋体',12,'normal'))

while not leftkey.down():screen.update()
dummy.clear()
# 新建上下管道
up_pip = Sprite('res/上管道.png',pos=(width,height//2))
down_pip = Sprite('res/下管道.png',pos=(width,-height//2))

bird = Sprite(shape=bimages,pos=(-100,0))  # 新建小鸟
bird.dy = 0                                # 垂直速度
bird.die = False                           # 描述死亡
def alt_costume():                         # 切换造型
    bird.nextcostume()                     # 下一个造型
    if bird.die == False:                  # 如果没死
        screen.ontimer(alt_costume,130)    # 130毫各后继续
alt_costume()

running = True                             # 控制while循环
clock = Clock()                            # 新建时钟对象
while running:
    if leftkey.down():bird.dy = 10         # 按左键跳
    bird.move(0,bird.dy)                   # 垂直移动
    if bird.ycor() < -height/2-10:
        running = False
    bird.dy -= 0.6
    
    # 上下管道移动
    up_pip.move(-2,0)
    if up_pip.xcor()<-width/2:             # 到了最左边移
        y = random.randint(-50,50)
        up_pip.reborn(width,y + height//2) # 移到最右边
    down_pip.move(-2,0)
    if down_pip.xcor()<-width/2:
        y = random.randint(-50,100)
        down_pip.reborn(width,y - height//2)

    # 鸟碰到上管道或下管道
    if bird.collide(up_pip,scale=0.8) or  \
       bird.collide(down_pip,scale=0.8):
        bird.die = True
        bird.play('res/punch.wav')
        bird.wait(0.1)
        break       
    clock.tick(60)
    
if bird.die:                               # 如果死了
    bird.left(90)
    while bird.ycor() > -height/2-10:
        bird.addy(-10)
        clock.tick(60)


d = Sprite(visible=False,pos=(0,100))
d.shape('res/cry.png')
d.stamp()
d.sety(-100)
d.write('Game Over',align='center',font=('楷体',32,'normal'))
screen.mainloop()
