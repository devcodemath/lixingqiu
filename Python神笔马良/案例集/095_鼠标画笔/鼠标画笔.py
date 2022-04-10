"""
   鼠标画笔.py
   本程序可以用鼠标指针在屏幕上画画儿。
"""
import turtle

screen = turtle.getscreen()
screen.setup(480,360)
screen.delay(0)

turtle.color('magenta')
turtle.pensize(3)
turtle.speed(0)
turtle.penup()
turtle.ht()

last_pos = None

def begindraw(event):
    global last_pos
    x = event.x - 240                   # 转换成海龟坐标系中的x坐标
    y = 180 - event.y                   # 转换成海龟坐标系中的y坐标
    if last_pos is not None:
        turtle.goto(last_pos)
        turtle.pendown()
        turtle.goto(x,y)

def enddraw(event):
    turtle.penup()
    last_pos = None
    
def follow_mouse(event):
    """本函数让小海龟面朝鼠标指针移动"""
    global last_pos
    screen.cv.unbind("<Motion>")         # 画布取消绑定鼠标移动事件
    x = event.x - 240                    # 转换成海龟坐标系中的x坐标
    y = 180 - event.y                    # 转换成海龟坐标系中的y坐标
    turtle.goto(x,y)
    last_pos = x,y                       # 记录上一次坐标
    screen.cv.bind("<Motion>",follow_mouse) # 画布绑定鼠标移动事件

screen.cv.bind("<Motion>",follow_mouse)     # 画布绑定鼠标移动事件
screen.cv.bind("<Button-1>",begindraw)      # 画布绑定鼠标单击事件
screen.cv.bind("<ButtonRelease-1>",enddraw) # 画布绑定鼠标释放事件
screen.mainloop()                           # 进入事件循环
