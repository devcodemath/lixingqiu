"""
   笑脸.py
"""
import turtle

def draw_circle(pos,radius):
    """以pos为中心点画圆"""    
    turtle.penup()
    turtle.goto(pos)
    turtle.fd(radius)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.right(90)
    turtle.bk(radius)    
    
turtle.color('blue')
turtle.pensize(2)

draw_circle((0,0),50)  # 以原点为中心画半径为50的圆
turtle.goto(-20,20)
turtle.dot(10)         # 这个点代表眼睛
turtle.goto(20,20)
turtle.dot(10)         # 这个点代表眼睛
turtle.goto(-20,-20)
turtle.right(45)
turtle.pendown()
turtle.circle(20,95)   # 这个弧代表嘴巴
turtle.ht()
turtle.done()
