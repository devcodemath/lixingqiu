"""
   摇一摇树.py
"""
import time
import random
import turtle

def yaoyiyao(x,y):
    """单击屏幕调用这个函数"""
    r = random.randint(5,10)
    for _ in range(r):
        dx = random.randint(-10,10)
        for item in t.items:      # 树的项目编号
            c.move(item,dx,0)     # 让项目水平偏移dx，垂直方向偏移0
        c.update()                # 更新显示
        time.sleep(0.1)
        
    
def draw_tree(length,level):
    """画二叉树
       基本画法是前进往左画一棵更小的树，这颗树画完后会自动回来，
       然后往右画一颗更小的树，最后回到起始点。
    """
    if level<1:return
    turtle.fd(length)                # 前进
    turtle.left(45)                  # 往左转45度
    draw_tree(length/1.6,level-1)    # 画更小的树
    turtle.right(90)                 # 右转90度
    draw_tree(length/1.6,level-1)    # 画更小的树
    turtle.left(45)                  # 往左转45度
    turtle.bk(length)                # 倒回到起始点

turtle.ht()                          # 隐藏海龟
turtle.delay(0)                      # 绘画延时为0毫秒
turtle.speed(0)                      # 动作速度为最快
turtle.width(2)                      # 画笔宽度为2
turtle.left(90)                      # 左转90度

draw_tree(100,6)
t = turtle.getturtle()            # 获取海龟本身
c = turtle.getcanvas()            # 获取画布对象
s = turtle.getscreen()            # 获取屏幕对象
s.onclick(yaoyiyao)               # 单击事件
s.mainloop()                      # 事件循环
