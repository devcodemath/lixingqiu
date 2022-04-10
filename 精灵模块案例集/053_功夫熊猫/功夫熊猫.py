"""
   功夫熊猫.py
"""

from sprites import *       # 从精灵模块导入所有命令

frames = ['frames/' + str(i) + ".png" for i in range(27)]

熊猫 = Sprite(shape=frames) # 新建功夫熊猫角色

while True:
    熊猫.nextcostume()      # 下一个造型
    熊猫.wait(0.1)          # 等待0.1秒
