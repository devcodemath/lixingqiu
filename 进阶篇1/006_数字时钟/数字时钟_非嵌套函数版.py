"""不用嵌套函数实现的电子时钟."""

from turtle import Turtle,Screen
import time

def make_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.title("模拟电子时钟")
    screen.bgpic("GreenSquareButton400.png")
    screen.setup(480,480)
    return screen

def watch():        
    current = time.localtime(time.time())  
    year = current.tm_year
    month = current.tm_mon
    day = current.tm_mday
    hour = current.tm_hour
    minute = current.tm_min
    second = current.tm_sec
    t.clear()
    info = str(year) + "年" + str(month)  + "月" + str(day) + "日"
    info = info + " " + str(hour) + "点" + str(minute) + "分" + str(second)+ "分"
    
    t.write(info ,align='center',font=("楷体",18,"normal"))
    t.screen.ontimer(watch,1000)
    
  

if __name__ == "__main__":

    screen = make_screen()
    t = Turtle(visible=False)
    t.color("brown")
    watch()
    screen.exitonclick()

