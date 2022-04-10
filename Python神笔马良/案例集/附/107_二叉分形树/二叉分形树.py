"""
   二叉分形树.py
"""
import turtle

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

turtle.width(2)                      # 画笔宽度为2
turtle.setheading(90)                # 朝向上的方向

turtle.speed(1)

draw_tree(100,4)

turtle.done()                        # 事件循环
