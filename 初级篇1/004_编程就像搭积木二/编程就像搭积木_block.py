"""编程就像搭积木,本程序定义若干个函数,演示函数式编程方法"""

from turtle import *

def init_screen():
    """初始化屏幕对象"""
    s = Screen()
    s.setup(480,360)
    s.delay(0)
    s.title("画矩形条")
    return s

def generate_turtle():
    """生成海龟对象"""
    t = Turtle()
    t.penup()
    t.pensize(4)
    t.setheading(90)  
    return t
    
def  draw_block(color,海龟,边长):
     """画正方形""" 
     海龟.color(color)
     海龟.begin_fill()
     for i in range(4):         
         海龟.fd(边长)
         海龟.lt(90)
     海龟.end_fill() 
         
def main():
    """主程序,请把下面冗余的代码定义成函数."""
    colorlist = ['red','orange','yellow','green','cyan','blue','purple','pink']
    screen = init_screen()                       #初始化屏幕对象
    g = generate_turtle()                        #产生海龟对象
    g.bk(100)
    k = 8
    while k > 0:
        pos = g.pos()
        for i in range(k):
            draw_block(colorlist[i],g,30)
            g.fd(30)
        g.goto(pos)
        g.setx(g.xcor() + 30)
        k = k - 1
    

"如果不是作为模块导入而运行,那么就运行main函数。" 
if __name__ == "__main__":    
    
    main()
    
    
