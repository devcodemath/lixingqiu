"""
   收拾玩具,本程序演示了如何继承Sprite类。
   程序操作方法：单击每个角色，把它们放入圆圈即可。
   
"""
from sprites import *

class Toy(Sprite):
    def __init__(self,shape=2,pos=(0,0),visible=True,
                 undobuffersize=1000,tag='sprite'):
        Sprite.__init__(self,shape=shape,pos=pos,visible=visible,
                        undobuffersize=undobuffersize,tag=tag)
        self.clicks = 0             # 描述单击次数
        self.status = ''            # 描述状态 
        
screen = Screen()                   # 新建屏幕

d = Sprite(visible=False)           # 新建画圆的精灵 
d.color('dodger blue')
d.pensize(4)
d.fd(200)
d.left(90)
d.pendown()
d.circle(200)                       # 画圆


toys = []                           # 新建列表
for i in range(10):
    t = Toy(i)                      # 新建玩具
    t.gotorandom()                  # 到随机坐标
    while t.distance(0,0) < 200:t.gotorandom()
    t.say('请单击我，而不是拖动我',1000,False)
    toys.append(t)                  # 加入列表 

leftkey = Mouse(1)
while True:
    for tt in toys:
        if leftkey.down() and tt.collide_mouse():
            while leftkey.down():screen.update()
            if tt.clicks==0 :
               tt.status = '跟随'
               tt.clicks += 1       # 单击数加1
            elif tt.clicks==1:
                 if tt.distance(0,0)<200:
                    tt.status = ''
                    tt.clicks -= 1     # 单击数减1
                    tt.say('放置完毕',1,False)

        if tt.status == '跟随':tt.goto(mouse_pos())

    screen.update()
        
