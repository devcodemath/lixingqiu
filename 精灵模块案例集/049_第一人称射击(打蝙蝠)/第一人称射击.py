"""
   第一人称射击.py
"""
from sprites import *
try:
    import pygame    
    pygame.mixer.init()
    fire_sound = pygame.mixer.Sound("audio/发射声.wav")
    cricket_sound = pygame.mixer.Sound('audio/cricket.wav')
except:
    import sys
    input("本程序需要pygame混音器支持以便配音,请先在cmd下用pip install pygame安装此模块。")
    
width,height = 480,360
screen = Screen()
screen.title('第一人称射击射蝙蝠by李兴球www.lixingqiu.com')
screen.bgpic('res/ghosthouse.jpg')
screen.setup(width,height)

batimages = ['res/bat1.png','res/bat2.png']   # 蝙蝠的两个造型
batindex = 0
bat = Sprite(visible=False,pos=(-50-width//2,100))
bat.dx = 3
bat.dy = 0
bat.alive = True
bat.show()
def bat_alt_costume():
    global batindex
    batindex = 1 - batindex
    bat.shape(batimages[batindex])
    screen.ontimer(bat_alt_costume,90)
bat_alt_costume()    

hole = Sprite(shape='res/Bullet_Hole.png',visible=False) # 洞角色

m1 = Mouse(1)           # 鼠标左键
m3 = Mouse(3)           # 鼠标右键
clock = Clock()         # 时钟对象 
start_stamp = False
while True:
    bat.move(bat.dx,bat.dy)
        
    # 蝙蝠碰到鼠标指针并且按下了鼠标左键       
    if bat.collide_mouse() and m1.down() and bat.alive:         
        bat.dy = -10                # 开始往下掉
        bat.alive = False
        try: cricket_sound.play()
        except:pass
        
    # 掉到地面就盖图章，留下尸体
    if bat.ycor() < random.randint(-200,-100):
        bat.dx = 0
        bat.dy = 0
        bat.setheading(random.randint(1,360))    # 随机设定方向
        bat.stamp()                              # 盖图章  
        bat.reborn(-500-width//2,100,3,0,delay=2)# 重生
        bat.alive = True                         
        bat.setheading(0)
        
    # 到了最右边就到最左边去重新开始
    if bat.xcor() > width//2 :
        bat.reborn(-500-width//2,100,3,0,delay=2)
        bat.alive = True
        bat.setheading(0)
    hole.goto(mouse_position())

    # 发射子弹，用盖图章留下弹洞，为防连续发射用了start_stamp变量
    if m1.down() and not start_stamp: # start_stamp决定每次只盖一个章 
        hole.stamp()
        start_stamp = True
        try: fire_sound.play()
        except: pass
        
    # 松开按键后
    if not m1.down():start_stamp = False

    clock.tick(60)
    

