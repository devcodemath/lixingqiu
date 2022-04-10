"""
   黑脉金斑蝶.py
   本程序主要学习全局变量和局部变量,以及用global申明全局变量的用法。
   在函数内定义的变量叫局部变量,在函数外定义的叫全局变量。
   Python规定，在函数内可以引用，但不能改变全局变量的值，
   如果要改变全局变量的值，则要显示的声明一个变量为全局变量。
"""
from sprites import *

PlaySound('Elements.wav',SND_ASYNC|SND_LOOP)  # 循环播放音乐

f = open("说明.txt")                          # 打开文件
c = f.read()                                  # 读取文件
f.close()                                     # 关闭文件
briefs = c.split('++++++++++')                # 以连加号分隔,返回列表

bgs = []                                      # 定义bgs列表
for i in range(1,14):                         # 在范围1,14迭代i      
    bgs.append('res/' + str(i) + ".png")      # 添加到列表

screen = Screen()                             # 新建屏幕
screen.setup(960,720)                         # 设定屏幕宽高    

index = 0                                     # 定义index变量
def alt_background():
    global index                              # 声明index是全局变量
    screen.bgpic(bgs[index])                  # 显示背景图   
    index = index + 1                         # index自增加1
    index = index % 13                        # index对13求余
    screen.ontimer(alt_background,20000)      # 20秒后再次调用函数
alt_background()                              # 调用alt_background函数

s = Sprite(visible=False,pos=(0,-720))        # 新建s角色

for i in range(len(briefs)):                  # 在范围内迭代i
    info = briefs[i]                          # 取索引为i的说明
    while s.ycor() < 720:                     # 当s的y坐标小于720  
        s.clear()                             # 清空所写
        s.write2(info)                        # 写字
        if s.ycor()==0:                       # 如果s的y坐标和0相等
            s.wait(10)                        # 等待10秒
        else:                                 # 否则
            s.wait(0.01)                      # 等待0.01秒 
        s.addy(1)                             # y坐标增加1
    s.sety(-720)                              # 设置y坐标为-720
s.home()                                      # 回到原点
s.write2('保护昆虫就是保护我们人类自己')      # 写阴影字
screen.mainloop()                             # 进入主循环

