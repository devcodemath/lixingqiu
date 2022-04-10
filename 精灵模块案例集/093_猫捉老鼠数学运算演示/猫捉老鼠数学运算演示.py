"""
   猫捉老鼠数学演示。
   猫在老鼠30米之远处发现了老鼠，现在老鼠要逃跑。猫一跳为2.5米，老鼠一跳1.2米。
   但在相同时间内，猫跳3次而老鼠能跑5次，求猫需要多少时间单位才能捉住老鼠。
   本程序演示了上面所说的这个过程。
"""
from sprites import *

distance = []
t = 0
startx = -200
cat_dist = startx +  t * 3 * 2.5
mouse_dist = startx + t * 5 * 1.2 + 30
distance.append((cat_dist,mouse_dist))
while cat_dist != mouse_dist:
    t += 1                                # 增加一个单位时间
    cat_dist = startx +  t * 3 * 2.5      # 算猫到起点的距离
    mouse_dist = startx + t * 5 * 1.2 + 30# 算鼠到起点的距离
    distance.append((cat_dist,mouse_dist))# 加入列表

screen = Screen()
screen.setup(480,200)

s = Sprite(visible=False)                 # 画线条的角色
s.bk(200)
s.dot(5,'red')
s.pendown()
s.fd(300)
s.penup()

cat = Sprite('res/cat1.png')              # 猫
mouse = Sprite('res/rat1.png')            # 老鼠 
cat.scale(0.5)
mouse.scale(0.5)
for d1,d2 in distance:
    cat.setx(d1)
    mouse.setx(d2)
    time.sleep(0.3)
s.goto(0,50)
s.write('捉到老鼠了',align='center')
