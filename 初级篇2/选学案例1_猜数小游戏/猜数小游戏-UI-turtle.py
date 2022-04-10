"""猜数小游戏-UI-turtle.py"""

from random import randint
from turtle import *
from tkinter import messagebox

game_title = "猜数小游戏"
max_number = 100
min_number = 1 
number = randint(min_number,max_number) # 在最小和最大数之间随机选择一个数

screen = Screen()
screen.setup(800,533)
screen.bgpic("th.png")
screen.title(game_title)

info1 = "Hello,我是计算机，欢迎来到猜数小游戏。"
info2 = "我会生成一个从1到100以内的整数，你猜猜它是多少吧。"
messagebox.showinfo(game_title, info1)
messagebox.showinfo(game_title, info2)

while True:
    answer = screen.numinput(game_title,"请输入整数：")
    if answer == None : continue 
    if int(answer) == number :
        messagebox.showinfo(str(number), "恭喜，你猜对了！" )         
        break
    if int(answer) < number:
        messagebox.showinfo(game_title, "小了！") 
        
    if int(answer) > number:
         messagebox.showinfo(game_title, "大了！") 

messagebox.showinfo(game_title, "游戏结束了。再见！！")
screen.bye()
        
