"""
   台阶图.py
"""
import turtle             # 导入海龟模块
    
turtle.width(2)           # 设定画笔宽度为2
 
for _ in range(5):        # 重复5次
    turtle.fd(50)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(90)
    
turtle.bk(250)           # 倒退250
y = turtle.ycor()+250    # 海龟y坐标的值加250
turtle.sety(y)           # 把y值设为海龟的y坐标

turtle.done()            # 海龟完事了 
