"""
   黑猫警长的射击.py
   本程序主要演示的是空格键的按键检测
"""
import time
from sprites import *

screen = Screen()                          # 新建屏幕
screen.setup(480,360)                      # 设定宽高
screen.bgcolor('dodger blue')              # 设定屏幕颜色
screen.title('黑猫警长的射击')             # 写上标题

cat = Sprite('猫.png')                     # 新建猫角色 
zd = Sprite('子弹.png')                    # 新建子弹角色
zd.left(30)                                # 子弹左转30度
zd.hide()                                  # 隐藏子弹

spacekey = Key('space')                    # 新建空格键按键
screen.listen()                            # 监听键盘按键

while True:
    # 如果按了空格键并且子弹是隐藏的
    if spacekey.down() and zd.ishide():
        zd.play('枪声')                    # 播放枪声
        x,y = cat.pos()                    # 获取猫的中心点坐标
        # 下面让x和y坐标增加,是为了让子弹移到枪口的位置
        x = x + 90                         # 枪口x坐标距离猫中心x坐标往右偏移90
        y = y + 75                         # 枪口y坐标距离猫中心y坐标往上偏移75
        zd.goto(x,y)                       # 子弹定位到x,y坐标(枪口坐标)
        zd.show()                          # 显示子弹
    if zd.isvisible(): zd.fd(5)            # 如果子弹是显示的则移动5个单位
    if zd.collide_edge():zd.hide()         # 如果子弹碰到到边缘则隐藏
    time.sleep(0.01)                       # 等待0.01秒 
    screen.update()                        # 更新屏幕显示

