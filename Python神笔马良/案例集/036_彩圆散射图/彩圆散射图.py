"""
   彩圆散射图
"""
import turtle                    # 导入海龟模块

turtle.bgcolor('black')          # 设定背景颜色        
turtle.color('yellow','red')     # 设画笔和填充色
turtle.shape('circle')           # 设定造型为圆形
turtle.hideturtle()              # 隐藏海龟
turtle.speed(0)                  # 设定移动速度为最快
turtle.delay(0)                  # 设定绘画延时为0毫秒

# 下面的for循环是画10根线条
for _ in range(10):              
    turtle.fd(1000)
    turtle.bk(1000)
    turtle.rt(36)

# 下面的代码是盖越来越大的图章，盖完后回到原点，再次重复
turtle.penup()
for _ in range(10):
    s= 0.5
    while s < 5:                    # 当s小于5的时候
        turtle.shapesize(s/2,s/2,2) # 设定造型比例
        turtle.stamp()              # 盖图章
        turtle.fd(20)               # 前进20个单位
        s = s + 0.5                 # s增加0.5
    turtle.goto(0,0)                # 回到原点
    turtle.right(36)                # 右转36度
    
turtle.done()                       # 事件循环
