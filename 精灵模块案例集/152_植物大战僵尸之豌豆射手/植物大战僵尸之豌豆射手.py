"""
   植物大战僵尸之豌豆射手.py
"""
from sprites import *

def spawn():
    """生成豌豆，会自动放在ps组中"""
    ps = Group('豌豆')
    if len(ps)<10:
        # 生成标签为豌豆的角色
        p = Sprite('豌豆.png',visible=False,tag='豌豆')
        x,y = shooter.pos()
        p.goto(x+20,y+18)
        p.show()                                  # 显示出来
    
screen = Screen()
screen.setup(640,480)
screen.bgpic('院子.png')
screen.title('植物大战僵尸之豌豆射手.py')

shooter = Sprite(shape='peas',pos=(-200,0))   # 生成射手

ps = Group('豌豆')                            # 新建豌豆组
counter = 0
while True:
    counter += 1    
    if counter % 20 == 0 :
        shooter.nextcostume()                 # 下一个造型
        spawn()                               # 生成一颗豆子
        
    [p.fd(5) for p in ps]                     # 每颗豌豆向前移动

    # 到了边缘的豆子就隐藏
    [p.ht() for p in ps if p.collide_edge()]
    # 如果豆子隐藏了,则再次从shooter位置出现
    [p.reborn(shooter.xcor()+20,shooter.ycor()+18) for p in ps if p.ishide()]
    time.sleep(0.01)
    
