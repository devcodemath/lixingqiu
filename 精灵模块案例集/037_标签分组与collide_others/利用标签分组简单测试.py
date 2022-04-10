from sprites import *    # 从精灵模块导入所有命令

screen = Screen()        # 新建屏幕 
bug = Sprite()           # 新建默认精灵，虫子

cat1 = Sprite(2,tag='cat')
cat1.goto(100,100)

cat2 = Sprite(2,tag='cat')
cat2.goto(-100,100)

ufo1 = Sprite(10,tag='ufo')
ufo1.goto(100,-100)

ufo2 = Sprite(10,tag='ufo')
ufo2.goto(-100,-100)

while True:
    screen.title("")
    bug.goto(mouse_pos())
    r1 = bug.collide_others('cat')
    if r1 : screen.title("碰到猫")
    r2 = bug.collide_others('ufo')
    if r2 : screen.title("碰到飞碟")
    
