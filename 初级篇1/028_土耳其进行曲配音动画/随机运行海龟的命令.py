"""随机运行海龟命令.py"""

from turtle import *
from random import randint,choice

color_list = ['red','orange','yellow','green','cyan','magenta']
code_list = ['fd','rt','lt','bk','dot']

screen = Screen()
screen.bgcolor("gray")

t = Turtle()                         # 新建海龟对象
while True:
    t.color(choice(color_list))
    command = choice(code_list)      # 从列表中随机挑选的命令,如fd,rt
    parameter = str(randint(1,10))   # 随机一个参数
    code = "t." + command + "(" + parameter + ")"  # 合成代码字符串
    exec(code)                       # 把字符串code当成代码来执行
