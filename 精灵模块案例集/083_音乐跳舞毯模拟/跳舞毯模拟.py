"""
   音乐跳舞毯模拟,当箭头滑过中间的箭头时，按相应的方向箭头即可加分。
   本程序也演示了如何播放多首背景音乐。
   注意音乐文件名下划线中的数字是时长，这时预先查看到设故意设成这样的。
   也可以用相关模块的命令读出wav的时长。
   由于借用了pygame的混音器，所以本程序正常运行还要安装pygame模块。
   共有8首背景音乐，2个声音效果。声音播放用了winsound模块的PlaySound命令(sprites模块封装)
   和pygame模块的混音器功能。
"""
from sprites import *                             # 从精灵模块导入所有命令
from pygame import mixer                          # 从pygame模块导入混音器

mixer.init()                                      # 初始化混音器
soundeffect = mixer.Sound('fairydust.wav')        # 实例化音频对象

Sprite(visible=False).play('dance celebrate.wav') # 封面时的音效
screen = Screen()
screen.setup(480,360)
screen.bgpic('res/cover.png')   
spacekey = Key('space')                           # 空格键
mouseleftkey = Mouse(1)                           # 鼠标左键
screen.listen()
while not (mouseleftkey.down() or  spacekey.down()):
    screen.update()   

screen.bgpic('res/stage-kiss.png')

arrowpng = 'res/绿箭头.png'
# 下面是用于碰撞的箭头,可以把它们设为完全透明
rightarrow = Sprite(shape=arrowpng,pos=(90,0))
leftarrow = Sprite(shape=arrowpng,pos=(-90,0))
leftarrow.right(180)
uparrow = Sprite(shape=arrowpng,pos=(-30,0))
uparrow.left(90)
downarrow = Sprite(shape=arrowpng,pos=(30,0))
downarrow.right(90)

# 下面是移动的箭头
rightarrow2 = Sprite(shape=arrowpng,pos=(90,-180))
leftarrow2 = Sprite(shape=arrowpng,pos=(-90,-280))
leftarrow2.right(180)
uparrow2 = Sprite(shape=arrowpng,pos=(-30,-2000))
uparrow2.left(90)
downarrow2 = Sprite(shape=arrowpng,pos=(30,-1000))
downarrow2.right(90)

score = 0
def rightreleased():
    global score    
    if rightarrow2.collide(rightarrow):
        rightarrow.left(1)
        score += 10
        effect((0,120),'res/add10.png',500)
        soundeffect.play()
def leftreleased():
    global score    
    if leftarrow2.collide(leftarrow):
        leftarrow.left(1)
        score += 10
        effect((0,120),'res/add10.png',500)
        soundeffect.play()
def upreleased():
    global score    
    if uparrow2.collide(uparrow):
        uparrow.left(1)
        score += 10
        effect((0,120),'res/add10.png',500)
        soundeffect.play()
def downreleased():
    global score    
    if downarrow2.collide(downarrow):
        downarrow.left(1)
        score += 10
        effect((0,120),'res/add10.png',500)
        soundeffect.play()
    
screen.onkey(rightreleased,"Right")
screen.onkey(leftreleased,"Left")
screen.onkey(upreleased,"Up")
screen.onkey(downreleased,"Down")

musics = ['music/01_99.wav','music/02_118.wav','music/03_96.wav',
          'music/04_329.wav','music/05_275.wav','music/06_141.wav',
          'music/07_118.wav','music/08_140.wav']
index = 0
m = Sprite(visible=False)
def playmusic():
    global index
    music = musics[index]
    m.play(music)   
    times = music.split('/')[-1].split('.')[0].split('_')[-1]
    times = int(times) * 1000
    index = index + 1
    if index < len(musics):
        screen.ontimer(playmusic,times)
playmusic()                           # 播放多首音乐 

clock = Clock()
while True:
    # 右方向箭头按键检测
    rightarrow2.addy(2)            
    if rightarrow2.ycor() > 180:
        rightarrow2.reborn(90,-180+random.randint(-300,0))
       
    # 左方向箭头按键检测
    leftarrow2.addy(2)            
    if leftarrow2.ycor() > 180:
        leftarrow2.reborn(-90,-180+random.randint(-500,0))
        
    # 上方向箭头按键检测
    uparrow2.addy(2)            
    if uparrow2.ycor() > 180:
        uparrow2.reborn(-30,-180+random.randint(-700,0))
        
    # 下方向箭头按键检测
    downarrow2.addy(2)            
    if downarrow2.ycor() > 180:
        downarrow2.reborn(30,-180+random.randint(-900,0))


    screen.title("得分："  + str(score))
    clock.tick(60)


