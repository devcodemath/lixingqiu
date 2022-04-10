"""
   一朵小花.py
"""
import turtle as t        # 导入海龟模块做为t
  
t.bgcolor('lime')         # 设定背景颜色 
t.pencolor('red')         # 设定画笔颜色为红
t.pensize(2)              # 设定画笔粗细为2

for _ in range(4):
    for _ in range(2):
        t.circle(101,-180)
        t.right(180)
    t.right(90)
t.done()
