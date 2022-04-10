"""
   下面的小猫有16个走路的造型，
   在这个动画中并不是通过nextcostume方法进行造型的切换,
   而是通过直接指定造型编号进行造型的切换的。
   
"""
from sprites import *                 # 从精灵模块导入所有命令 

frames = [f'cats/Walk{i:02d}.png' for i in range(16)]  # 共有16个造型

cat = Sprite(shape=frames,visible=False)  # 新建序列帧为frames的小猫
cat.scale(0.5)                        # 缩小
cat.show()                            # 显示出来
cat.shapeindex(15)                    # 指定造型编号为15

cat.saycolor('blue')                  # 说话泡泡中字的颜色 
cat.saybordercolor('orange')          # 说话泡泡边框的颜色
info = '你好,欢迎使用Python精灵模块，\n'
info = info + '使用这个模块能非常简单地制作小动画小游戏，\n'
info = info + '非常适合于小学生学习Python知识'

cat.say(info,10000,wait=False)        # 显示说话泡泡，不必等待说完
cat.wait(1)                           # 等待1秒中

while True:                           # 当成立的时候 
    for i in range(16):               # 迭代i变量16次
       cat.shapeindex(i)              # cat切换到编号为i的造型    
       cat.wait(0.1)                  # cat等待0.1秒
