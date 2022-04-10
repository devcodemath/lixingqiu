from sprites import Sprite,Screen,txt2image

screen = Screen()

c = screen.textinput('请输入一个汉字','')

# 把所输入的汉字转换成zi.png图片
txt2image(c,'zi.png',fontsize=66)

sp = Sprite('zi.png',pos=(0,200))  # 新建角色,使用zi.png图
sp.wait(1)                         # 等待1秒

dy = 0                             # 垂直速度
while True:
    sp.right(1)
    sp.move(0,dy)                  # 移动角色                    
    if sp.ycor() < -200:           # 小于-200则反弹
        dy = -dy
    else:                          # 否则dy减小
        dy = dy -0.1
    sp.wait(0.01)                  # 等待0.01秒
