"""
   像素碰撞程序.py
   本程序演示在python精灵模块中新增的pixelcollide命令。
   它演示了一个角色对另一个角色的像素级碰撞检测。
   pixelcollide命令返回的信息比较丰富。
   在下面的程序中，我们把mover叫主碰方，dummy叫被碰方。
   那么像素碰撞所返回的信息包括以下内容，它是一个4元组。
   第一个数据表示第一个碰撞点的坐标，第二个数据是主碰方在碰撞点的像素值。
   第三个数据是被碰方在碰撞点的像素值。
   第四个数据是两个角色矩形重叠的左上角坐标和右下角坐标及重叠区域面积。
   运行程序后，可以单击鼠标左键，让mover旋转。
   本程序需要python精灵模块1.35版本以上支持。
   安装最新版本请用cmd打开命令提示符管理员窗口输入以下命令：
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites  --upgrade
   
"""
from sprites import *

screen = Screen()                       # 新建屏幕

wer = Sprite(visible=False,pos=(0,150))
dummy = Sprite('xiao2.png')            # 中间的角色
dummy.say('我是dummy',delay=2)
mover = Sprite('xiao3.png')            # 用鼠标指针操作的角色

k = Mouse()                            # 鼠标左键
while 1:
    mover.goto(mouse_pos())            # 移到鼠标指针的坐标
    r = mover.pixelcollide(dummy)      # 对mover和dummy进行像素碰撞
    if r:
        a,b,c,d = r
        wer.clear()                     # 清除以前所画
        wer.goto(0,150)
        wer.write('碰撞点坐标：' + str(a),align='center')
        wer.addy(-25)
        wer.write('mover在碰撞点的颜色值：' + str(b),align='center')
        wer.addy(-25)
        wer.write('dummy在碰撞点的颜色值：' + str(c),align='center')
        wer.addy(-25)
        wer.write('mover和dummy矩形碰撞重叠区域：' + str(d),align='center')
        screen.title(r)
    if k.down():                        # 单击鼠标左键，旋转mover
        while k.down():screen.update()  # 没松开就一直更新屏幕
        mover.left(90)                  # 否则左转90度
    screen.update()                     # 更新屏幕显示
