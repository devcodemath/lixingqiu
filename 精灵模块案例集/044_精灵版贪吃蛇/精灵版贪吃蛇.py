"""
   精灵版贪吃蛇.py
   本程序是用图章功能制作的贪吃蛇小游戏。
   在精灵模块中重定义了stamp命令。它可以让图章在一定时间后自动被清除。
   
"""
from sprites import *

screen = Screen()
screen.resizable()
screen.setup(480,360)
screen.bgpic('res/sky.png')

bug = Sprite()
bug.scale(0.6)

upkey = Key('Up')
downkey = Key('Down')
leftkey = Key('Left')
rightkey = Key('Right')

ball = Sprite(1,pos=(200,100)) # 在(200,100)放个球

wait = 0.5                     # 0.5除0.1等于5，所以开始有5个身子 
screen.listen()
while True:
    if upkey.down():bug.setheading(90)
    if downkey.down():bug.setheading(-90)
    if rightkey.down():bug.setheading(0)
    if leftkey.down():bug.setheading(180)
     
    bug.fd(20)
    if bug.collide(ball):           # 如果碰到球
        wait += 0.1                 # 图章们的等待时间加0.1秒
        x = random.randint(-240,240)
        y = random.randint(-180,180)
        ball.reborn(x,y,delay=1)    # 1秒后在x,y坐标显示
        
    bug.stamp(wait)                 # 在wait秒后图章会自动删除
    time.sleep(0.1)                 # 等待0.1秒

