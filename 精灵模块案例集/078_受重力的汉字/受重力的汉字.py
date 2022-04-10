"""
   受重力的汉字,本程序把字符串转换成角色,然后让它们做自由落体运动。
   到了最底下后会反弹，角色们还是可以拖动的。
   
"""
from sprites import *       # 从精灵模块导入所有命令

string = '风火轮编程'

images = []
for zi in string:
    filename = f'res/{zi}.png'
    images.append(filename)
    txt2image(zi,filename,fontsize=36)

screen = Screen()
screen.bgcolor('pink')       # 背景颜色为粉红色

zigroup = Group('zi')        # 新建组,标签为zi
y = 200
for i in range(len(string)):
    x = -100 + i * 50
    # 下面角色的标签为zi,它们会自动加入到zigroup
    s = Sprite(shape=images[i],tag='zi',pos=(x,y))
    s.dy = 0   
    
clock = Clock()              # 新建时钟对象
while True:
    for zi in zigroup:
        zi.move(0,zi.dy)                          
        if zi.ycor() < -200:  # 小于-200就反弹
            zi.dy = -zi.dy
        else:                 # 否则dy减小
            zi.dy -= 1        # 加速度为1
        clock.tick(120)
        
        
