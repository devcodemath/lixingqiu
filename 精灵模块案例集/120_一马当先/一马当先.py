"""
   一马当先.py
   本程序是赛马演示动画,其中一匹马跑得更快,
   配乐为土耳其进行曲
"""
import random                          # 导入随机模块
from sprites import *                  # 从精灵模块导入所有命令

screen = Screen()                      # 新建屏幕
screen.setup(1024,480)                 # 设定宽高
screen.titlebar(False)                 # 隐标题栏
screen.draggable()                     # 按中键拖
screen.addpopup()                      # 右键菜单
screen.bgpic('grass.png')              # 设背景图

horse = Sprite("images",visible=False) # 新建角色 
horse.scale(0.4)                       # 缩小为0.4倍
horse.show()                           # 显示出来  
horse.setx(-450)                       # 设置x坐标
horse.速度 = random.randint(2,3)       # 自定义属性名字叫速度
horse.play('土耳其进行曲.wav')         # 播放音乐

hs = [horse]                           # 新建列表
for y in range(-150,151,50):           # 迭代y,-150,-100,-50,0,50,100,150
    h = horse.clone()                  # 克隆一匹马
    h.速度 = random.randint(2,3)       # 设置马的速度
    h.sety(y)                          # 设置马的y坐标 
    hs.append(h)                       # 把这匹马添加到列表

xm = random.choice(hs)                 # 随机从列表中挑一匹马             
xm.速度 = random.randint(4,6)          # 把xm马的速度设为更大

end = Sprite(shape='square')           # 终点线角色
end.color('red')                       # 把它设为红色
end.shapesize(20,0.2)                  # 对宽度和高度进行变形
end.setx(450)

time.sleep(2)
running = True                         # 定义逻辑变量
while running:                         # 当running为True的时候
    for h in hs:                       # 每一匹马
        h.fd(h.速度)                   # 马前进h.速度
        h.nextcostume()                # 马换造型
        if h.collide(end):             # 如果有一匹马碰到终点线
            running = False            # 把running设为False
            break                      # 中断for循环
    time.sleep(0.01)                   # 等待0.01秒

screen.mainloop()                      # 进入主循环,不断刷新组件
