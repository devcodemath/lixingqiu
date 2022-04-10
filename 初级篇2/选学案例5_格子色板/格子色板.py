"""格子色板.py 本程序画彩色格子"""

from turtle import Turtle, Screen

def draw_square(haigui, length, color):
    """画单一颜色方块图形"""
    haigui.color(color)
    haigui.pendown()
    haigui.begin_fill()
    for _ in range(4):
        haigui.forward(length)
        haigui.left(90)
    haigui.end_fill()
    haigui.penup()
     

def draw_board(haigui,position,rows,cols,length):
    """根据行列数与起点及边长画格子
       haigui : 海龟对象
       rows : 行数
       cols : 列数
       length:格子的边长
    """
    colors = 'red','orange','yellow','green','cyan','blue','purple','magenta'
    amounts = len(colors)
    haigui.goto(position)
    index = 0
    for row in range(rows):           # 行
        for col in range(cols):       # 列
            draw_square(haigui,length,colors[index])
            index = index + 1
            index = index % amounts
            haigui.fd(length)        # 前进length
        haigui.bk(length * cols)     # 倒退length*cols
        haigui.right(90)             # 右转90度
        haigui.fd(length)            # 前进length
        haigui.left(90)              # 左转90度

if __name__ == "__main__":

    t = Turtle(visible=False)
    t.penup()
    t.screen.delay(0)
    draw_board(t,(-200,200),5,5,40)
    t.screen.exitonclick()
        
