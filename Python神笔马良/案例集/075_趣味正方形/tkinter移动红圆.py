"""
   tkinter移动红圆.py
"""
from tkinter import *
from time import sleep

root = Tk()
root.title('画布项目移动测试程序')

canvas = Canvas(root,width=480,height=360)
canvas.pack()

square = canvas.create_oval(10,10,50,50,fill='red')

for _ in range(100):
    canvas.move(square,1,0)  # 在水平方向移动1个单位
    canvas.update()
    sleep(0.01)
