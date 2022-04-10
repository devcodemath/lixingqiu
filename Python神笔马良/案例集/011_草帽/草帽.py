"""
   草帽.py
"""
import turtle           # 导入海龟模块

turtle.delay(20)        # 设定绘画延时为20毫秒
turtle.speed(1)         # 设定移动速度为最慢
for _ in range(72):     # 重复72次
    for _ in range(5):  # 重复5次
        turtle.fd(50)   # 海龟前进50个单位
        turtle.rt(50)   # 海龟右转50度
        turtle.bk(80)   # 海龟倒退80个单位
    turtle.lt(95)       # 海龟左转95度
    
turtle.done()           # 海龟做完了 
