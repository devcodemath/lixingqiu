from turtle import *

def 画正方形(g,bc):
    for _ in range(4):   #可以用下划线做为变量名称
       g.fd(bc) 
       g.rt(90)

t = Turtle()
画正方形(t,100)
