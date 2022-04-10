"""
   大炮打蝙蝠.py
   蝙蝠大队来袭。它们要干什么？难道要去散布新型冠状病毒？
   一定要阻止它们！通过这个案例，你将会学习到如何通过鼠标操作角色左右移动,
   以及如何对列表的每一个成员进行碰撞检测。
"""
from sprites import *
from pygame import mixer                  # 从pygame导入混音器

mixer.init()
shootsnd = mixer.Sound('榴弹炮.wav')      # 实例化发射音效

mixer.music.load('Melee- Menu.wav')       # 加载背景音乐
mixer.music.play(-1,0)                    # 从头开始循环播放音乐

screen = Screen()                         # 新建屏幕
screen.setup(480,360)
screen.bgpic('背景1.BMP')
screen.title('大炮打蝙蝠_Python精灵模块_李兴球博客')

canon = Sprite('大炮.png',pos=(0,-150))   # 新建大炮
canon.left(90)
canon.ondrag(None)                        # 不可拖动

bomb = Sprite('bomb.png',visible=False)   # 新建炮弹
bomb.left(90)

bats = {}                                 # 蝙蝠字典,项目编号对应角色的字典
batimgs = ['bat1-a.png','bat1-b.png']
mbat = Sprite(batimgs,pos=(-260,150),visible=False)

leftkey = Mouse()                         # 鼠标左键
shooting = False
clock = Clock()                           # 时钟对象
counter = 0
while True:
    counter = counter + 1
    if counter % 20 ==0 :
        b = mbat.clone()
        b.isalive = True               # 自定义属性,活着的为真
        b.show()
        bats[b.turtle._item] = b
    if counter % 8 == 0 :
        [bat.nextcostume() for bat in bats.values()]
    for bat in list(bats.values()):
        if bat.isalive:
           bat.fd(5)
        else:
           bat.addy(-8)
        if bat.xcor() > 240 or bat.ycor()<-180:            
            bats.pop(bat.turtle._item)
            bat.remove()
            
    mx,my = mouse_pos()
    canon.setx(mx)
    if leftkey.down() and shooting==False:
        shooting = True
        bomb.goto(canon.pos())
        bomb.addy(25)
        bomb.show()
        shootsnd.play()
    if bomb.isvisible():                # 如果是可见的
       bomb.addy(8)                    # 往上移动10个单位
       items = bomb.overlap_with(list(bats.values()))
       if items :
           print('items',items)
           for item in items:
              bats[item].isalive=False
       bomb.right(25)                   # 往右旋转25度 
       if bomb.ycor() > 180:            # 如果y坐标大于180
           bomb.hide()                  # 隐藏
           shooting = False             # 设为False,这样才可以再次发射
       
    screen.update()
    clock.tick(60)
