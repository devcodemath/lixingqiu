"""
   瞎猫走方格,
   本程序画了一个10X10的宽高为50的格子,
   然后瞎猫随机选择一个方向,直到走出格子,如此重复。
"""
from sprites import *

rows = 10
cols = 10
length = 50
# 行数,列数,格子宽度,格子高度,返回每个格子中心点坐标
Sprite(visible=False).draw_grid2(rows,cols,length,length)

cat = Sprite(2)
cat.width(4)
cat.scale(0.5)
cat.color('red')
while True:
    running = True
    cat.clear()    
    cat.home()
    cat.pendown()
    while running:
        r = random.randint(0,3)
        cat.setheading(r*90)
        cat.fd(length)
        if abs(int(cat.xcor())) > length*cols//2 or \
           abs(int(cat.ycor())) > length*rows//2 :
            running = False
        cat.wait(0.1)
    cat.penup()
    print(cat.xcor(),cat.ycor())
    cat.wait(2)
