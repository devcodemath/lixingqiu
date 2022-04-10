"""
   弹跳扇子.py
   你好，如果你读懂了本程序，在其它地方运用了，
   请注明创意或原理来自李兴球博客，谢谢。
"""
import time
import turtle

turtle.speed(0)
turtle.left(30)
turtle.color('blue')
turtle.bgcolor('yellow')
turtle.setup(480,360)
turtle.title('弹跳扇子by李兴球')
turtle.hideturtle()
turtle.penup()

turtle.sety(50)

# 开始画扇子
turtle.pendown()
for _ in range(120):
    turtle.fd(100)
    turtle.bk(120)
    turtle.fd(20)
    turtle.left(1)

time.sleep(1)                     # 等待1秒钟
turtle.delay(0)                   # 设定绘画延时为0毫秒 

dy = 0
t = turtle.getturtle()            # 得到海龟对象本身
canvas = t.screen.cv              # 得到画布对象

while True:
    # 把所画的每个项目都往下移
    for item in t.items:          # 遍历每个项目 
        canvas.move(item,0,dy)   
    t.screen.cv.update()          # 更新画布显示
    time.sleep(0.01)              # 等待0.01秒  
    if dy  > 7 :                  # 如果dy大于7，就让dy取反
        dy = -dy
    else:                         # 否则dy增加1  
        dy = dy + 0.1
