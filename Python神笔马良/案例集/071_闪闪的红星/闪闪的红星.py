"""
   闪闪的红星.py
"""
import time
import turtle

def xsleep(n):
    """防止无响应窗口出现的延时函数"""
    begintime = time.time()
    while time.time() - begintime < n:
        turtle.update()
        
def draw_star(length):
    """画填充五角星"""
    turtle.begin_fill()
    for _ in range(5):
        turtle.fd(length)
        turtle.lt(144)
    turtle.end_fill()

turtle.color('red')
turtle.bgcolor('black')
turtle.ht()
turtle.tracer(0,0)            # 关闭动画显示与设定绘画延时为0毫秒
while True:
    turtle.clear()            # 清除所画的
    xsleep(0.5)               # 等待0.5秒左右 
    draw_star(150)            # 画星星
    turtle.update()           # 更新显示
    xsleep(0.5)               # 等待0.5秒左右
