"""
   九星连珠.py
"""
import turtle

turtle.shape('circle')         # 设定海龟造型为圆形
turtle.color('gray')           # 设定画笔和填充颜色为灰色
turtle.setup(900,389)          # 设定窗口宽度和高度
turtle.bgpic('sun.png')        # 设定背景图片
turtle.title('九星连珠')       # 设定窗口标题 
turtle.speed(0)                # 设定移动速度为最快
turtle.penup()                 # 抬笔

# 画中横线
turtle.setx(-380)              # 设置x坐标
turtle.pendown()               # 落笔
turtle.setx(450)               # 设置x坐标
turtle.penup()                 # 抬笔 

# 画上斜线
turtle.setx(-380)              # 设置x坐标
turtle.left(6)                 # 左转6度
turtle.pendown()               # 落笔 
turtle.fd(900)                 # 前进900个单位
turtle.penup()                 # 抬笔
turtle.goto(-380,0)            # 到达坐标

# 画下斜线
turtle.right(12)               # 右转12度
turtle.pendown()               # 落笔 
turtle.fd(900)                 # 前进900个单位
turtle.penup()                 # 抬笔
turtle.setheading(0)           # 设定方向为0度

# 水星
turtle.color('gold','gray')    # 设画笔和填充颜色
turtle.shapesize(0.6)          # 设定变形比例 
turtle.goto(-300,0)            # 到达坐标
turtle.stamp()

# 金星
turtle.color('gold','brown')   # 设画笔和填充颜色
turtle.shapesize(1)            # 设定变形比例 
turtle.fd(50)                  # 前进50个单位
turtle.stamp()                 # 盖图章

# 地球

turtle.color('green','blue')   # 设画笔和填充颜色
turtle.shapesize(1.5)          # 设定变形比例
turtle.fd(50)                  # 前进50个单位
turtle.stamp()                 # 盖图章

# 火星
turtle.color('brown','red')    # 设画笔和填充颜色
turtle.shapesize(1.2)          # 设定变形比例
turtle.fd(50)                  # 前进50个单位
turtle.stamp()                 # 盖图章

# 木星
turtle.color('brown','orange') # 设画笔和填充颜色
turtle.shapesize(9)            # 设定变形比例 
turtle.fd(130)                 # 前进130个单位
turtle.stamp()                 # 盖图章

# 土星(0.5,0.6,0.7))
turtle.color('brown',(0.8,0.9,0.7))
turtle.shapesize(6)
turtle.fd(170)
turtle.stamp()

# 天王星
turtle.color('blue',(0.5,0.8,0.7))
turtle.shapesize(3)
turtle.fd(120)
turtle.stamp()

# 海王星
turtle.shape('circle')
turtle.color('blue',(0.5,0.6,0.9))
turtle.shapesize(4)
turtle.fd(100)
turtle.stamp()

# 冥王星
turtle.color((0.5,0.4,0.1))
turtle.shapesize(2)
turtle.fd(80)
turtle.stamp()

turtle.done()                # 海龟做完了
