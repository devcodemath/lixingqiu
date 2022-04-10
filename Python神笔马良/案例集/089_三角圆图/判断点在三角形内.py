"""
   判断点在三角形内.py
"""
import turtle
    
def _isinside(x1, y1, x2, y2, x3, y3, x, y):
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

def inside(x,y):
    x1,y1 = p[0][0],p[0][1]
    x2,y2 = p[1][0],p[1][1]
    x3,y3 = p[2][0],p[2][1]
    if  _isinside(x1,y1,x2,y2,x3,y3,x,y):
        print('在里面')
    else:
        print('不在里面')
    

turtle.begin_poly() 
turtle.fd(200)
turtle.lt(120)
turtle.fd(200)
turtle.lt(120)
turtle.fd(200)
turtle.lt(120)
turtle.end_poly()
p = list(turtle.get_poly())
p.pop()
print(p)

s = turtle.getscreen()
s.onclick(inside)
draw_circle((0,0),100)

