"""
   查找重叠命令.py
   
   角色的find_overlapping命令就是查找重叠命令。
   它用来查找和角色最小矩形重叠的其它项目。简单理解就是有没有和其它项目发生碰撞。
   这些项目包括其它角色、所画的线条、填充的颜色块、盖的图章、画的圆点。
   返回的结果是这些项目的编号,是一个集合。本命令主要用来进行碰撞检测。
   本程序需要精灵模块v1.28版本以上支持。
"""
from sprites import *             # 从精灵模块导入所有命令

title = 'find_overlapping命令测试程序'
s = Sprite()                      # 新建角色
s.color('magenta')                # 设定颜色
s.goto(0,200)
s.write2(title)
s.width(3)                        # 画笔宽度
s.goto(0,0)
s.write('风火轮编程')             # 写文字 
s.fd(160)

s.dot(100,'green')                # 打绿色圆点
s.bk(300)
s.pendown()                       # 落笔
for x in range(3):                # 重复3次
  s.fd(100)                       # 前进100
  s.lt(90)                        # 左转90度
s.penup()                         # 抬笔 

while True:                       # 当成立的时候 
    s.goto(mouse_pos())           # 移到鼠标指针 
    t =  s.find_overlapping()     # 查找有没有和s的矩形重叠的东西 
    if t:print(t)                 # 有就打印它们的编号


