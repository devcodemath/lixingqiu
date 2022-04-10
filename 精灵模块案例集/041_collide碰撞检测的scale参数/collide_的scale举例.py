"""
   collide碰撞检测的scale参数举例。
   请修改下面collide中的scale值的大小，
   仔细观察老鼠碰到猫时和绑定盒的关系。
   
"""

from sprites import *

images = ['res/rat1.png','res/rat2.png']

screen = Screen()                    # 新建屏幕
screen.bgcolor("dodger blue")        # 屏幕涂色

tom = Sprite(shape='res/rat1.png')   # 新建老鼠

index = 0                            # 索引号为0
def alt_costume():
    global index                     # 声明为全局变量
    tom.shape(images[index])         # 设定造型
    index = 1 - index                # 更换索引号
    screen.ontimer(alt_costume,200)  # 200毫秒后再次运行alt_costume
alt_costume()

cat = Sprite(shape='res/cat1.png')   # 新建小猫
while 1:
    tom.heading(mouse_pos())         # 朝向鼠标指针
    if tom.distance(mouse_pos()) > 50:# 距离大于5则前进
        tom.fd(1)
    if tom.collide(cat,scale=0.1):    # 老鼠碰到猫，猫就说话
        cat.say("晚餐送上门了",1,False)
