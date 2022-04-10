"""编程就像搭积木.py,本程序定义若干个函数。"""
import turtle

def init_screen():
    """初始化屏幕对象,返回屏幕对象。"""
    s = turtle.Screen()
    s.setup(480,360)
    s.delay(0)
    s.title("画多边形")
    s.bgcolor("white")
    return s

def generate_turtle():
    """生成海龟对象，并且返回它。"""
    t = turtle.Turtle()
    t.pensize(4)  
    return t
    
def  draw_square(color,海龟,边数,边长):
     """画多边形"""     
     angle = 360/边数
     for i in range(边数):
         海龟.color(color)
         海龟.fd(边长)
         海龟.lt(angle)
         
def main():
    """主程序"""
    colorlist = ['red','orange','yellow','green','cyan','blue','purple','magenta']
    amounts = len(colorlist)                     # 颜色数量
    screen = init_screen()                       # 初始化屏幕对象
    g = generate_turtle()                        # 产生海龟对象
    g.bk(200)                                    # 海龟倒退200个单位

    for _ in range(5):         
        for i in range(amounts):
            draw_square(colorlist[i],g,i+3,10)   # 画多个正多边形           
        g.fd(100)
    screen.exitonclick()
     
"如果不是作为模块导入而运行,那么就运行main函数。" 
if __name__ == "__main__":    
    
    main()
     
    
    
