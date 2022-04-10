'''水波纹模拟一,请建立Ripple类,重新编程,实现同样的效果.'''
import glob
from turtle import Turtle,Screen      

def draw(x,y):     
    """画圆圈"""
    screen.onclick(None)              # 取消事件绑定
    t = Turtle(visible = False)       # 建隐藏的对象
    t.color(29,153,231)               # 设定颜色
    t.pensize(4)                      # 画笔宽度
    t.penup()                         # 抬起笔来
    t.speed(0)                        # 速度为最快
    t.radius = 10                     # 初始半径为10
    def ripple():
        """使用屏幕的定时器功能重复画圆"""
        t.goto(x,y)                    # 到圆心
        t.fd(t.radius)                 # 前进radius
        t.left(90)                     # 左转90
        t.pendown()                    # 落笔
        t.circle(t.radius)             # 画圆
        t.penup()                      # 抬笔
        t.radius = t.radius + 10       # 半径增加10
        if t.radius < 500:
            screen.ontimer(ripple,50) # 再次画更大的圆
        else:
            screen.onclick(draw)       # 重新绑定单击事件
    ripple()
    
def animate_screen():
    """不断地切换屏幕背景"""
    global bg_index
    screen.bgpic(waveimages[bg_index])
    bg_index = bg_index + 1
    bg_index = bg_index % bg_amounts
    screen.ontimer(animate_screen,100)

def clear_draw(x,y):
    """清除所有画的笔迹"""
    for t in screen.turtles():t.clear()
    
if __name__ == "__main__":

    bg_index = 0                        #背景索引号    
    waveimages = glob.glob("waves/*.png")
    bg_amounts = len(waveimages)        #背景数量
    
    screen = Screen()
    screen.title('水波纹模拟-面向过程') # 写上窗口标题
    screen.setup(800,600)               # 设定窗口大小
    screen.bgcolor('black')             # 背景颜色为黑
    screen.delay(0)                     # 绘画延时为0
    screen.colormode(255)               # 颜色模式为255
    screen.onclick(draw)                # 单击左键调用draw
    screen.onclick(clear_draw,3)        # 单击右键调用此函数
    animate_screen()                    # 不断切换背景
    screen.mainloop()                   # 进入主循环

 
