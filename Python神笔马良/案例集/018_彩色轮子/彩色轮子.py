"""
   彩色轮子.py
   注意本例中,颜色为原点对称。
"""
import turtle
from coloradd import colorset       # 从颜色增加模块导入colorset命令

screen = turtle.getscreen()
screen.bgcolor('light cyan')
screen.colormode(255)               # 设置颜色模式为RGB255
screen.delay(0)
turtle.speed(0)
turtle.pensize(2)

def draw():
    """重复画36个正方形"""
    for x in range(36):             # 在36的范围内迭代x  
       for _ in range(4):
          for _ in range(100):
              距离 = turtle.distance(0,0)
              c = colorset(距离+160) 
              turtle.color(c)
              turtle.fd(1)
          turtle.right(90)
       turtle.right(10)
       
screen.tracer(0)                      # 关闭动画
draw()
screen.update()                       # 显示刷新  

screen.mainloop()                     # 事件循环 
