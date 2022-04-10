"""新闻联播字幕动画.py"""
from time import sleep
from turtle import Screen,Turtle

ziti = ("楷体",16,"normal")
width,height = 800,450

screen = Screen()
screen.bgcolor("black")
screen.title("新闻联播字幕动画")
screen.setup(width,height)
screen.bgpic("bg.png")
screen.delay(0)
screen.update()
sleep(1)

t = Turtle(visible=False)
t.speed(0)                # 速度最快
t.penup()                 # 抬笔
t.color("cyan")           # 设为青色
t.goto(0,-10-height//2)   # 坐标定位

index = 0
m1 = "来自潘朵啦星球消息,那里的原始人掌握了高科技,准备向宇宙移民。"
m2 = "来自火星消息，地球2代已经认为自己是火星人了。"
m3 = "来自月球消息，月球的微生物是远古时候从地球抛向太空的微生物。"
m4 = "来自中国消息，孔子号战舰已经飞出银河系，向着白马座方向飞去。"
m5 = "来自微信群消息，公安部门逮捕了一批过节不发红包的群主。"
m6 = "来自风火轮少儿编程的消息，本程序下载网址：www.scratch8.net。"
m7 = "来自编程娃娃消息，幼儿编程已经普及，胎教编程教育产品正在开发。"
m8 = "本次播报由风火轮少儿编程赞助，欢迎下次观看，单击关闭窗口。"

infos = [m1,m2,m3,m4,m5,m6,m7,m8]

while index < len(infos):
    "下面的for循环让字符串上移。"
    for i in range(60):
        t.clear() 
        t.write(infos[index],align='center',font=ziti)
        screen.update()
        sleep(0.01)
        t.sety(t.ycor() + 1)        
    sleep(6)
    "下面的for循环让字符串下移。"
    for i in range(60):
        t.clear() 
        t.write(infos[index],align='center',font=ziti)
        screen.update()
        sleep(0.01)
        t.sety(t.ycor() - 1)       
     
    index = index + 1
    
t.clear()
screen.exitonclick()

    
