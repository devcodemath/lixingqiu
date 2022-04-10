"""
   太空虫子。
   太空外星害虫来袭,小虫子被赋予光荣任务去消灭它们。
   可是它没有武器，只有去撞死它们。
   请按上下左右方向箭头,消灭所有害虫!
   
"""

from sprites import *

width,height = 600,760
screen = Screen()               # 新建屏幕
screen.setup(width,height)      # 屏幕宽高
screen.bgcolor('black')         # 背景颜色
screen.title('太空虫子_by www.lixingqiu.com')

# 铺设星空背景
star = Sprite(shape='star',visible=False)
star.color('white')             # 星星为白色
for _ in range(50):
    star.gotorandom()
    star.scale(max(0.01,random.random()/10))
    star.stamp()                # 星星盖图章
 
pest_group = Group('pest')      # 新建所有害虫组
rows = 8                        # 行数 
cols = 8                        # 列数 
startx = -200                   # 起始x坐标
starty = 300                    # 起始y坐标
for r in range(rows):           # 迭代rows
    for c in range(cols):       # 迭代cols
        x = startx + c * 60     # 形成x坐标
        y = starty - r * 40     # 形成y坐标
        p = Sprite(shape='res/pest.png',pos=(x,y),tag='pest')
        p.dy = 0                # 垂直速度为0   
        p.da = 0                # 加速度为-0.5

# 新建木条，作为虫子的托盘   
woodbar = Sprite('res/woodbar.png',pos=(0,-320))

bug = Sprite(pos=(0,-200))      # 新建虫子
bug.left(90)                    # 左转90度
bug.dx = 0                      # 水平速度
bug.dy = 0                      # 垂直速度

leftkey = Key("Left")           # 实例化左方向箭头
rightkey = Key("Right")         # 实例化右方向箭头
upkey = Key("Up")               # 实例化上方向箭头
downkey = Key("Down")           # 实例化下方向箭头

screen.listen()
clock = Clock()                 # 新建时钟对象
while True:
    wdx = 0                     # 描述木条和虫子水平速度 
    if leftkey.down(): wdx = -8
    if rightkey.down():wdx = 8
    woodbar.addx(wdx)
    左,上,右,下 = woodbar.bbox()
    if 左 < -width//2 or 右 > width//2:
        woodbar.addx(-wdx)
        wdx = 0
    if bug.collide(woodbar):    # 如果碰到木条
        bug.dx = 0
        bug.dy = 0
        bug.addx(wdx)           # 和木条同步x坐标
        bug.setx = woodbar.ycor() + 10
        if upkey.down():        # 按了向上箭头跳
            bug.dx = wdx
            bug.dy = 30         # 这里决定了跳的高度 
    else:
        bug.dy -= 0.8
        if abs(bug.xcor()) + 20 > width//2:
            bug.dx = -bug.dx
            bug.dy += 10        # 碰到左右两边弹得更高
            
    bug.move(bug.dx,bug.dy)
    pests = bug.collide_others('pest',scale=0.5)
    if pests:
        for p in pests: p.da = 0.8
           
    for p in list(pest_group):  # 移动每只害虫
        p.move(0,p.dy)
        p.dy -= p.da
        if p.ycor() < -height//2-20:p.remove()
        
    if len(pest_group) == 0 :
        txt2image('游戏成功结束!','res/success.png',
                  fontsize=32,color=(0,255,255,228))
        suc = Sprite(shape='res/success.png',pos=(0,300))
        suc.glide((0,0))
        break

    if bug.ycor() < -height//2:
        txt2image('失  败!','res/fail.png',
                  fontsize=32,color=(255,3,33,228))
        Sprite(shape='res/fail.png',pos=(0,0))
        break
        
    screen.update()
    clock.tick(60)

screen.mainloop()
