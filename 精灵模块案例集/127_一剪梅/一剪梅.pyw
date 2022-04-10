"""
   一剪梅.py
   本程序主要介绍角色的play方法,它能带歌词文件!
"""
from sprites import *                  # 从精灵模块导入所有命令
from random import choice              # 从随机模块导入choice命令

screen = Screen()                      # 新建屏幕
screen.setup(706,500)                  # 设置屏幕宽高
screen.bgpic('封面.png')               # 设置屏幕背景图
screen.bgcolor('dodger blue')          # 设置屏幕背景色 
screen.titlebar(False)                 # 关闭标题栏
screen.addpopup()                      # 增加右键菜单
screen.draggable()                     # 按中键可拖动窗口

f = open('评论.txt')                   # 打开文件
c = f.read()                           # 读文件
f.close()                              # 关闭文件
lines = c.split('\n')                  # 以换行分隔文件,返回列表

bug = Sprite(visible=False)            # 新建隐藏的虫子角色
bug.color('blue')                      # 颜色为蓝色
bug.sety(-140)                         # 设置y坐标为-140
bug.play('一剪梅(费玉清).wav','歌词.txt')

w = Sprite(visible=False)              # 新建w角色,写评论的
w.sety(-200)                           # 设置y坐标为-200

# 下面代码段每隔20秒显示一条对这首歌曲的评论。
while True:                            # 当成立的时候
    w.wait(20)                         # 等待20秒钟
    w.clear()                          # 清空w所写
    cm = '随机评论：' + choice(lines)
    w.write(cm,align='center',font=('宋体',12,'normal'))
    
