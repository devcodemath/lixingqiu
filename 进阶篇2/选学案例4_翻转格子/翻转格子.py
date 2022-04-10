"""翻转格子.py。单击就会翻转颜色的格子，本程序演示了基本原理，
无论是用直接用tkinter还是pygame模块制作，程序逻辑都是一样的。
"""
from turtle import *
 
def draw(x,y):    
    """单击屏幕任何位置时调用本函数。首先把坐标进行转换，
    然后得到所单击的行列号，最后实现翻转逻辑后调用画矩形函数。"""    
    y = (240 - y)          # y坐标转换(以左上为原点坐标系)
    x = (240 + x)          # x坐标转换   
    r = int(y // height)   # 求行号
    c = int(x // width)    # 求列号    
    grids_flag[r][c] = 1 - grids_flag[r][c] # 翻转逻辑在这里实现
    draw_rect(t,r,c)       # 调用画矩形的函数 

def draw_rect(t,r,c):
    """使用海龟t在r行c列填充矩形"""    
    x1 = c * width - 240   # x坐标转换回去(以中间为原点坐标系)
    y1 = -r * height + 240   
    t.goto(x1,y1)
    if grids_flag[r][c]== 0 : # 可设一逻辑字典，则不需要if判断
        t.color("white")      # 是零就填充白色
    else:
        t.color("black")      # 否则填充黑色        
    # 开始填充画矩形    
    t.begin_fill()            # 开始填充
    for i in range(2):        # 迭代i两次
        t.fd(width)           # 前进width
        t.rt(90)              # 右转90度
        t.fd(height)          # 前进height
        t.rt(90)              # 右转90度
    t.end_fill()              # 结束填充   

if __name__ == "__main__":
    
    size = screen_width,screen_height = 480,480     
    screen = Screen()
    screen.setup(*size)
    screen.title("翻转格子_李兴球海龟画图版")
    screen.delay(0)

    rows,cols = 16,12             # 行列数量
    width = screen_width// cols   # 每个格子宽度  
    height = screen_height// rows # 每个格子高度  
    grids_flag = []               # 格子标志表,0表示白色,1黑
    [grids_flag.append([0]*cols) for r in range(rows)]       

    t = Turtle(visible=False)     # 新建用来画格子的海龟
    t.penup()                     # 抬笔
    t.speed(0)                    # 速度最快
    screen.onclick(draw)          # onclick绑定draw函数
    screen.mainloop()             # 进入主循环



