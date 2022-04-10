from turtle import *

def draw_star(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(5):
        t.fd(100)
        t.right(144)

def change_color(x,y):        # 也可以先把屏幕的颜色模式设为255,然后随机生成r,g,b,就不用global了
    global index,amounts
    index = index + 1
    index = index % amounts
    t.color(colors[index])
    
def 画正方形(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for  i in range(4):
        t.fd(100)
        t.right(90)


colors = ['red','orange','yellow','green','cyan','blue','purple','brown','magenta']
index = 0
amounts = len(colors)

screen = Screen()

t = Turtle()

screen.onclick(画正方形)    
screen.onclick(draw_star,2)
screen.onclick(change_color,3)
screen.mainloop()


 
