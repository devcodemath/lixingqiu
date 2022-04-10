"""
   简易夺旗游戏(python像素级碰撞检测之颜色碰撞)
   按上下左右方向箭头操作小虫子去碰到小旗子,游戏就胜利了,
   否则如果碰到黑色,游戏就失败了!
   本程序需要python精灵模块V1.35以上版本支持。演示的是在V1.35版本中的像素级碰撞命令。
   它的名字叫pixelcollide。参数为角色和阈值。本命令只支持都为图形的角色。
   请在cmd命令提示符下面输入以下命令安装python精灵模块。
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites  --upgrade
"""
from sprites import *           # 从精灵模块导入所有命令

def collidecheck():
    
    r = bug.pixelcollide(bg)    # 对bug和bg进行像素极碰撞检测
    
    if r:
        # 如果碰到的是绿色则成功了
        if r[2] == (0,255,51):
            print('成功')
            return 1
        else:
            return 2
    else:
        return 3
            
screen = Screen()               # 新建屏幕
screen.setup(960,720)           # 设置屏幕宽高

bg = Sprite('背景1.png')        # 新建背景角色
bg.ondrag(None)                 # 让角色不可拖动
bug = Sprite(pos=(-430,-280))   # 新建虫子角色
bug.rotatemode(2)
leftkey = Key("Left")           # 向左方向箭头
rightkey = Key("Right")         # 向右方向箭头 
upkey = Key("Up")               # 向上方向箭头
downkey = Key("Down")           # 向下方向箭头
screen.listen()                 # 监听屏幕按键

while True:
    if leftkey.down():          # 按左方向箭头往左移
        bug.setheading(180)
        bug.fd(5)
        r =  collidecheck()
        if r == 1:
            break
        elif r == 2:
            bug.bk(5)
    elif  rightkey.down():        # 按右方向箭头往左移
        bug.setheading(0)
        bug.fd(5)
        r =  collidecheck()
        if r == 1:
            break
        elif r == 2:
            bug.bk(5)
    elif  upkey.down():           # 按上方向箭头往左移
        bug.setheading(90)
        bug.fd(5)
        r =  collidecheck()
        if r == 1:
            break
        elif r == 2:
            bug.bk(5)
    elif downkey.down():          # 按下方向箭头往左移
        bug.setheading(-90)
        bug.fd(5)
        r =  collidecheck()
        if r == 1:
            break
        elif r == 2:
            bug.bk(5)
        
    screen.update()
print(r)
screen.title('game over')
screen.mainloop()
        
