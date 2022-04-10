"""
   三角圆图.py
"""
import turtle

def draw_circle(pos,radius):
    """以pos为中心点，radius为半径画圆"""
    pe = 2 * 3.14159 * radius             # 周长
    step = pe/360                         # 每度需要位移的量
    turtle.penup()
    turtle.goto(pos)
    turtle.fd(radius)
    turtle.left(90)    
    for _ in range(360):
        if intriangle(turtle.xcor(),turtle.ycor()):
            turtle.pendown()            
        else:
            turtle.penup()
        turtle.fd(step)
        turtle.left(1)
    turtle.penup()
    turtle.right(90)
    turtle.bk(radius)
    
def _isinside(x1, y1, x2, y2, x3, y3, x, y):
    """判断x,y点是否在由x1,...y3组成的三角形内"""
    def crossProduct(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1

    if crossProduct(x3-x1, y3-y1, x2-x1, y2-y1) >= 0:
        x2, x3 = x3, x2
        y2, y3 = y3, y2
    if crossProduct(x2-x1, y2-y1, x-x1, y-y1) < 0:
        return False
    if crossProduct(x3-x2, y3-y2, x-x2, y-y2) < 0:
        return False
    if crossProduct(x1-x3, y1-y3, x-x3, y-y3) < 0:
        return False
    return True

def intriangle(x,y):
    """判断点x,y是否在三角形内"""
    x1,y1 = p[0][0],p[0][1]
    x2,y2 = p[1][0],p[1][1]
    x3,y3 = p[2][0],p[2][1]
    if  _isinside(x1,y1,x2,y2,x3,y3,x,y):
        return True
    else:
        return False
    
turtle.speed(0)
turtle.delay(0)
turtle.penup()
turtle.pensize(2)
# 画一个三角形，获取它们的顶点坐标
turtle.begin_poly()                        # 开始记录顶点
turtle.fd(200)
turtle.lt(120)
turtle.fd(200)
turtle.lt(120)
turtle.fd(200)
turtle.lt(120)
turtle.end_poly()                          # 结束记录顶点
p = list(turtle.get_poly())                # 转换成列表
p.pop()
# 求出三角形中心点坐标，以这个为圆心画圆
centerx = (p[0][0] + p[1][0] + p[2][0])/3
centery = (p[0][1] + p[1][1] + p[2][1])/3
center = centerx,centery

s = turtle.getscreen()                    # 得到屏幕
s.onclick(intriangle)                     # 绑定单击事件
for radius in range(4,120,10):            # 画一些圆,超出三角范围则不画
    draw_circle(center,radius)
turtle.ht()
turtle.done()
