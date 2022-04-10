"""
   天空飞来的鸽子.py
   本程序有模拟3D效果,表现鸽子由远及近的效果是让它的大小不断变大,
   并且y坐标不断地减小,本程序最后还有角色之间的对话。
"""
from sprites import *                     # 从精灵模块导入所有命令

screen = Screen()                         # 新建屏幕
screen.setup(800,600)                     # 设定屏幕宽高
screen.bgpic('boardwalk.png')             # 设定屏幕背景
screen.title('天空飞来的鸽子')            # 设定屏幕标题 

frames = ['dove1.png','dove2.png']        # 鸽子造型表
dove = Sprite(frames,pos=(0,420))         # 新建鸽子角色
dove.scale(0.05)                          # 缩放角色
for s in range(1,150):                    # 在范围内迭代s 
    dove.scale(s/600)                     # 缩放角色
    dove.addy(-3)                         # 往下移3个单位
    dove.nextshape()                      # 下一个造型 
    dove.wait(0.1)                        # 等待0.1秒

def alt_costume():
     """鸽子不断切换造型"""
     dove.nextshape()                     # 下一个造型
     screen.ontimer(alt_costume,200)      # 200毫秒后再次运行alt_costume 
alt_costume()                             # 调用切换造型函数

cat = Sprite(shape='cats',pos=(-600,-200))# 新建小猫角色
cat.play('喵.wav')                        # 播放声音 
cat.scale(0.4)                            # 缩放角色
for _ in range(80):                       # 在范围80内迭代_
    cat.nextcostume()                     # 下一个造型
    cat.fd(5)                             # 前进5个单位
    cat.wait(0.1)                         # 等待0.1秒
cat.costumeindex(0)                       # 设定猫的造型索引为0
cat.saycolor('red')                       # 设定说话文字的颜色为红
cat.saybordercolor('yellow')              # 设定说话边框颜色为黄
cat.say('你好')                           # 小猫说你好
dove.say('你也好')                        # 鸽子说你也好

screen.mainloop()                         # 进入主循环
