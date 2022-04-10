"""
   新型冠状病毒泡泡堂游戏.py
   本程序借用了pygame的混音器模块，所以需要安装pygame模块。
   需要精灵模块1.33版支持请卸载老版本，重新安装最新版本的精灵模块。
   程序中迷宫房间是画出来的，当然虫子是不能穿越过去，也不能碰到病毒...
   按上下左右键操作虫子移动,按空格键放炸弹。
"""

from sprites import * 
from pygame import mixer

def draw_frame(obj,margin):
    """用obj角色画边框,margin为边距
       本函数用for循环直接画一个正方形也可以。
    """
    sw = obj.screen.window_width()
    sh = obj.screen.window_height()
    bug.topleft()            # 移到左上角
    bug.addy(-margin)   
    x,y = bug.position()  
    cors = [(x+sw,y),(x+sw,y+margin),(x,y+margin)]
    f1 = bug.polygon(cors)
    
    bug.bottomleft()         # 移到左下角      
    x,y = bug.position()  
    cors = [(x+sw,y),(x+sw,y+margin),(x,y+margin)]
    f2 = bug.polygon(cors)
    
    bug.addy(margin)    
    x,y = bug.position()  
    cors = [(x+margin,y),(x+margin,y+(sh-2*margin)),(x,y+(sh-2*margin))]
    f3 = bug.polygon(cors)

    bug.addx(sw-margin)    
    x,y = bug.position()  
    cors = [(x+margin,y),(x+margin,y+(sh-2*margin)),(x,y+(sh-2*margin))]
    f4 = bug.polygon(cors)
    return [f1,f2,f3,f4]

def draw_cross(obj,length):
    """画十字架"""
    d = length/2
    bug.goto(-d,d)
    x,y = bug.position()
    cors = [(x+length,y),(x+length,y+2*length),(x,y+2*length)] 
    p1 = bug.polygon(cors)

    bug.goto(-d-2*length,-d)
    x,y = bug.position()
    cors = [(x+5*length,y),(x+5*length,y+length),(x,y+length)] 
    p2 = bug.polygon(cors)
    
    bug.goto(-d,-d-2*length)    
    x,y = bug.position()
    cors = [(x+length,y),(x+length,y+2*length),(x,y+2*length)] 
    p3 = bug.polygon(cors)
    return [p1,p2,p3]
    
def draw_squares(obj,length):
    """画4个正方形"""
    items = []
    for _ in range(4):
        i = bug.polygon(4,length)
        items.append(i)
        bug.fd(length*5)
        bug.rt(90)
    return items

width = 800
height = 600
screen = Screen()
screen.bgcolor('black')
screen.setup(width,height)
screen.title('新型冠状病毒泡泡堂游戏')
screen.bgpic('封面.png')

leftkey = Key('Left')
rightkey = Key('Right')
upkey = Key('Up')
downkey = Key('Down')
spacekey = Key('space')
screen.listen()

PlaySound('audios/泡堂开场音乐.wav',SND_ASYNC)
starttime = time.time()
while time.time() - starttime < 6 :
    screen.update()
    if spacekey.down():break
screen.bgpic('nopic')
PlaySound(None,SND_PURGE)
PlaySound('audios/泡泡堂小区音乐.wav',SND_ASYNC|SND_LOOP)

mixer.init()                      # 初始化混音器
bombsound = mixer.Sound('audios/BOMB1.wav')
placesound = mixer.Sound('audios/zoop.wav')

bomb = Sprite('bombs',visible=False)
bomb.scale(0.5)

w = 100
bug = Sprite(visible=False)       # 虫子角色,首先是隐藏的
bug.color('pink','pink')
items1 = draw_frame(bug,w/2)      # 用虫子画紧挨着屏幕的边框
items2 = draw_cross(bug,w/1.5)    # 用虫子画十字架
bug.goto(-w/2 - w,w/3 + w)
items3 = draw_squares(bug,w/1.5)  # 用虫子画四个正方形
items1.extend(items2)
items1.extend(items3)
print(items1)                     # items1是障碍物列表的项目编号
frames = items1                   # 取一个别名
# 上面的frames就是items1,代表所有障碍物.

bug.color('gray')
bug.goto(0,240)
info = '''本游戏代码有210行，Python精灵模块开发,作者:李兴球，
迷宫是画出来的,按上下左右键操作虫子移动,按空格键放炸弹。
'''
bug.write(info,align='center')
bug.color('black')
bug.goto(0,-290)
info = '''Python精灵模块基于海龟画图模块开发,
作者亦是李兴球。博客：www.lixingqiu.com'''
bug.write(info,align='center')

bug.goto(100,100)
clock = Clock()
bug.show()

cors = [(-100,100),(-100,-100),(265,2),(179,-107),(300, 101),
        (0,-219),(273,-213),(263, -140),(-258, 0),(-116,222)]
vsitems = []                       # 存储每个病毒项目编号的列表
vsgroup = Group('virus')           # 病毒组
for cor in cors:
    virus = Sprite(shape='res/病毒.png',pos=cor,tag='virus')
    virus.rotatemode(1)
    vsitems.append(virus.turtle._item)
    
result = None                      # 描述游戏成功或失败 
running = True                     # 描述游戏主循环
allow = True                       # 是否能放炸药？
counter = 0                        # 炸药的造型计数器
def check_bomb():
    """炸弹有从0到10共11个造型,这个函数会每隔0.1秒检测一次炸弹,
       根据它的可见性决定其行为。如果炸弹是可见的，那么counter是从0开始。
       这个时候要让炸弹切换到索引为0的造型，等待1秒，让counter增加1。
       然后在3秒内每隔一秒切换一次造型。
       3 秒过后，播放爆炸声，这个时候又是以每隔0.1秒切换造型的。
    """
    global counter,allow,running
    if running == False:return
    if bomb.isvisible():
        if counter == 0 :         # 刚放的时候等待1000毫秒后，开始切换造型 
            screen.ontimer(check_bomb,1000)
            counter += 1
        elif counter < len(bomb._costumes):
           bomb.nextcostume()     # 切换到下一个造型     
           if counter < 3:        # 在3秒内，每隔1秒切换一次造型，这样就能显示3，2，1
               screen.ontimer(check_bomb,1000)               
           else:
               if counter==3:bombsound.play()   # 刚好到了3秒，则播放爆炸声
               screen.ontimer(check_bomb,100)   # 接下来就是0.1秒切换一次造型。         
           counter += 1
        elif counter == len(bomb._costumes):    # 爆炸完后，隐藏炸弹
           bomb.hide()
           bomb.shapeindex(0)                   # 切换到索引为0的造型
           allow = True                         # 充许下次能被放置
           counter = 0                          # 计数器归零
           screen.ontimer(check_bomb,100)
    else:
        screen.ontimer(check_bomb,100)
check_bomb()

while running:    
    if leftkey.down():                          # 如果按左键， 
        bug.setheading(180)                     # 虫子朝左的方向
        bug.fd(5)                               # 移动5个单位
        if bug.overlap_with(items1):bug.bk(5)   # 如果碰到了障碍物，则倒退
    if rightkey.down():                         # 如果按了右方向箭头 
        bug.setheading(0)                       # 让虫子朝右的方向
        bug.fd(5)                               # 移动5个单位
        if bug.overlap_with(items1):bug.bk(5)   # 如果碰到了障碍物，则倒退
    if upkey.down():                            # 如果按了上方向箭头 
        bug.setheading(90)                      # 让虫子朝上的方向              
        bug.fd(5)                               # 移动5个单位
        if bug.overlap_with(items1):bug.bk(5)   # 如果碰到了障碍物，则倒退
    if downkey.down():                          # 如果按了下方向箭头 
        bug.setheading(-90)                     # 让虫子朝下的方向 
        bug.fd(5)                               # 移动5个单位 
        if bug.overlap_with(items1):bug.bk(5)
    if spacekey.down() and allow == True :    # 按空格键，并且allow为真，则放炸药
        print('放炸弹')
        placesound.play()                     # 播放置的音效
        bomb.goto(bug.position())             #  炸药移到虫子的坐标
        bomb.show()                           # 显示炸药
        allow = False                         # 这个变量为假了，下次按空格键就无效了 
    # 下面的v代表一个病毒
    for v in list(vsgroup):                   # 防止动态改变vsgroup所以加list
        v.fd(2)                               # v前进2个单位
        if v.overlap_with(frames):v.right(180)# 如果碰到了障碍物，则向后转
        # 如果病毒碰到了炸药，炸药正在爆炸，则删除病毒
        if v.overlap_with(bomb) and bomb._costume_index>2:
            v.remove()
    # 如果虫子碰到了炸药，并且炸药正在爆炸，则游戏结束。    
    if bug.overlap_with(bomb) and bomb._costume_index > 2:
        running = False
        result = False

    if bug.overlap_with(vsitems):             # 如果虫子碰到了任何一个病毒，
        running = False
        result = False
    if len(vsgroup) == 0 :                    # 如果病毒全部炸死了 
         running = False
         result = True
    screen.update()
    clock.tick(60)

print(result)
bug.wait(0.5)
if result:
    print('显示成功的封面')
    screen.clear()
    screen.bgpic('成功.png')
else:
    print('显示失败的封面')
    screen.clear()
    screen.bgpic('失败.png')
    
screen.mainloop()






