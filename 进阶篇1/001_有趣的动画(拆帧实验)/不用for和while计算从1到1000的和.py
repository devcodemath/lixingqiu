"""不用for和while计算从1到1000所有自然数的总和"""

from turtle import *

screen = Screen()
screen.setup(0,0)

i = 0
总和 = 0
def add():
    global i,总和
    i = i + 1
    总和  = 总和 + i
    if i<1000:
        screen.ontimer(add,0)
    else:
        print("从1到1000所有自然数的和为：",总和)

add()
    
