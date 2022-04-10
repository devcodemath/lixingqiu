"""数字时钟_嵌套函数版.py
请把本程序改造成不用嵌套的函数实现"""

from turtle import Turtle,Screen
import time

def main():
    ziti = ("楷体",18,"normal")
    screen = Screen()
    screen.bgcolor("white")
    screen.title("模拟数字时钟")
    screen.bgpic("GreenSquareButton400.png")
    screen.setup(480,480)
    t = Turtle(visible=False)
    t.color("brown")
    def watch():
        cut = time.time()            # 获取当前时间
        current = time.localtime(cut)# 返回结构化时间对象 
        year = current.tm_year       # 获取年份        
        month = current.tm_mon       # 获取月份
        day = current.tm_mday        # 获取日子
        hour = current.tm_hour       # 获取小时
        minute = current.tm_min      # 获取分钟
        second = current.tm_sec      # 获取秒数
        t.clear()                    # 海龟擦除所写
        info = str(year) + "年" + str(month) + "月" + str(day) + "日"
        info = info + " " + str(hour) + "点" + str(minute) + "分"
        info = info + str(second)+ "分"        
        t.write(info ,align='center',font=ziti) # 写上组装好的字符串
        t.screen.ontimer(watch,1000)            # 1秒钟后再次运行watch        
    watch()
    t.screen.exitonclick()                      # 单击屏幕关闭窗口

if __name__ == "__main__":

    main()

