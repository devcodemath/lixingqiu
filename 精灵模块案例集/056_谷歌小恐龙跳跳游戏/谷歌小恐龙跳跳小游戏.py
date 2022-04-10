"""
   谷歌小恐龙跳跳游戏.py
   按向上方向箭头操作小恐龙避开仙人掌即可
"""
from sprites import *

width,height = 480,360     # 定义宽高
screen = Screen()          # 新建屏幕
screen.bgpic('地面.png')   # 背景图片
screen.setup(width,height) # 设定宽高
screen.sety(-150)          # 图片下移
screen.title('谷歌浏览器小恐龙跳跳游戏by李兴球www.lixingqiu.com')

long = Sprite('小恐龙.png',visible=False)
long.scale(0.5)            # 造型缩小
long.setx(-100)            # 设x坐标
long.dy = 0                # 垂直速度
long.da = -0.5             # 加 速 度
upkey = Key('Up')          # 实例化向上键
long.show()                # 显示小恐龙角色

cactus = Sprite('仙人掌.png',pos=(480,-130))
cactus.scale(0.5)          # 变小 

screen.listen()            # 监听按键
clock = Clock()            # 建时钟对象
running = True
while running:
    cactus.move(-10,0)     # 仙人掌往左移 
    # 如果到了最左边,移到最右边的坐标
    if cactus.xcor()<-width//2:
        cactus.setx(random.randint(width,2*width))
        
    # 如果碰到恐龙,则游戏结束
    if cactus.collide(long,0.3):
        running = False
        
    long.addy(long.dy)     # 恐龙做自由落体运动  
    if long.ycor()>-120:   # 如果y坐标大于-120则继续落     
        long.dy += long.da
    else:                  # 否则停止落下
        long.dy = 0
        if upkey.down():   # 如果在地面时按了向上方向箭头
            long.dy = 10   # 垂直速度设为10
            
    screen.move(-8,0)      # 背景图片向后移8个单位
    if screen.xcor() < -width//2:
        screen.setx(width//2)
    screen.update()        # 刷新屏幕显示 
    clock.tick(60)         # 固定fps为60

d = Turtle(visible=False)  # 用于写game over的海龟对象
d.write('Game Over',align='center',font=('arial',32,'normal'))
screen.mainloop()          # 游戏主循环
