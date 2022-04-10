"""海龟赛跑小动画"""

__author__ = "lixingqiu"
__date__ = "2018/11/29"

from turtlerun import * 
 
screen = init_screen()                 #初始化屏幕
t = draw_racetrack()                   #画跑道，返回画跑道的海龟对象
turtles = generate_player()            #产生选手
run(turtles,t)                         #开始比赛，跑

screen.exitonclick()                   #单击关闭窗口


