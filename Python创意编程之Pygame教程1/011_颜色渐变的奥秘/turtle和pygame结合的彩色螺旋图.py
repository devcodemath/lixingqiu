"""
  turtle和pygame结合的彩色螺旋图.py
   本程序演示如何让颜色的色相部分产生渐变。
"""
import turtle              # 导入海龟模块
from math import *         # 从数学模块导入函数
from pygame import Color   # 从pygame导入Color类
    
def coloradd(color,dh):
    """
       颜色增加函数，本函数把颜色的色相进行增加,其它指标不变。
       color：Color实例化后的颜色
       dh：一个int,色相增加的值
    """
    h,s,v,a = color.hsva   
    h = h + dh             # 色相增加
    h = h % 360            # 不能超过360
    color.hsva = h,s,v,a   # 设定颜色的hsva值
    return Color(*color)   # 返回颜色实例

width,height = 480,360
screen = turtle.getscreen()
screen.setup(width,height)
screen.title("turtle和pygame结合的彩色螺旋图www.lixingqiu.com")
screen.colormode(255)
screen.delay(0)

turtle.width(30)
yanse = Color('red')

for i in range(2200):
    turtle.color(yanse[:-1])
    turtle.fd(i)
    turtle.rt(35)
    yanse = coloradd(yanse,1)

screen.mainloop()

