"""
   蝴蝶飞啊飞.py
   本程序演示如何新建动画角色
"""
from sprites import  *             # 从精灵模块导入所有命令

width,height = 480,360             # 定义宽高变量
screen = Screen()                  # 新建屏幕
screen.setup(width,height)         # 设定屏幕宽高
screen.bgpic('res/sky.png')        # 设定屏幕背景

# 在res文件夹有b1.png和b2.png两张向右造型的蝴蝶图片
rights = ['res/b1.png','res/b2.png'] # 两帧图形
                
b = Sprite(shape=rights)           # 新建动画角色
b.rotatemode(1)                    # 左右翻转模式  

while True:
    b.fd(10)                       # 前进10个单位 
    b.nextcostume()                # 下一个造型  
    b.bounce_on_edge()             # 碰到边缘就反弹
    b.wait(0.1)                    # 等待0.1秒 
