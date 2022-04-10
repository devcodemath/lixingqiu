from turtle import Screen,Turtle  # 从海龟画图导入Screen函数和Turtle类

screen = Screen()                 # 新建屏幕
screen.setup(800,600)             # 设置屏幕宽和高
screen.delay(0)                   # 绘画延时为0
screen.bgcolor("black")           # 背景以为黑色

def draw_snow(length):            # 画雪花函数
 
    for i in range(8):            # 重复8次  
        t.fd(length)              # 前进length 
        for j in range(8):
            t.fd(length/4)
            for k in range(8):
                t.fd(length/8)
                t.bk(length/8)
                t.rt(45)
            t.bk(length/4)            
            t.rt(45)
            
        t.bk(length)              # 后退length
        t.rt(45)                  # 右转45度

t = Turtle()                      # 新建海龟对象
t.pencolor("white")               # 画笔颜色为白色

t.begin_poly()                    # 开始记录顶点 
draw_snow(200)                    # 画雪花
t.end_poly()                      # 结束记录顶点
p = t.get_poly()                  # 得到顶点坐标元组
t.clear()                         # 清除所画图形
screen.addshape("snow",p)         # 给形状列表添加snow形状,形状列表可以由screen.getshapes()得到
t.shape("snow")                   # 设定t的形状为snow
 
while True: t.rt(1)
