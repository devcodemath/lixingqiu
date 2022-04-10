"""
   移动汉字贺卡.py
   运行程序后会弹出文本输入对话框,要你输入贺词。
   如果不输入贺词，则会有默认的贺词。
   然后用鼠标单击任一处，贺词就会变成一个个的海龟对象。

"""
import os
import time
from txt2image import *
from random import randint
from turtle import RawTurtle,Shape,Turtle,Screen
from winsound import PlaySound,SND_ASYNC,SND_LOOP
from PIL import Image,ImageFont,ImageDraw,ImageTk
 
def bounce_on_edge(self):
    """给RawTurtle类新增碰到边缘就反弹的方法"""
    sw = self.screen.window_width()
    sh = self.screen.window_height()
    x = self.xcor()
    y = self.ycor()    
    if x > sw/2 or x < -sw/2:             # 到了最右边或最左边
        self.seth(180 - self.heading())   # 改变方向
    elif y  > sh/2 or y < -sh/2:          # 到了最上边或最下边 
        self.seth( -self.heading())

RawTurtle.bounce_on_edge = bounce_on_edge # 新增方法 
    
Photo = ImageTk.PhotoImage                # 只是为了缩短代码而设的别称
screen = Screen()
screen.delay(0)
screen.bgcolor('black')
screen.setup(480,720)
screen.title('移动汉字贺卡by李兴球，网址:www.lixingqiu.com')

zi = screen.textinput('输入框','请输入贺词')
if zi==None or zi=="": zi =  '风火轮编程祝本群所有人员身体健康'
# 下面一行代码通过txt2image把汉字转换成pillow图形对象
# 再用ImageTk.PhotoImage把它包装成Shape类能用的图形对象
shapes = [Photo(txt2image(z,fontsize=28,color='blue')) for z in zi]

def clickevent(x,y):
    if shapes:
        sp = shapes.pop(0)            # 从shapes列表弹出第一个PhotoImage对象
        c = Shape('image',sp)         # 新建类型为image的造型
        screen.addshape(str(c),c)     # 把造型添加到造型字典
        z = Turtle(shape=str(c),visible=False)        
        z.penup()
        z.speed(0)       
        z.seth(randint(180,360))
        z.goto(x,y)
        z.stamp()
        z.showturtle()
    else:
        PlaySound('卓依婷-迎春花.wav',SND_LOOP|SND_ASYNC)
        screen.onclick(None)
        screen.bgpic('鱼.png')
        g = Turtle(visible=False)
        g.penup()

        g.sety(-20)
        g.color('magenta')
        s = 'Python值得你拥有'
        g.write(s,align='center',font=('',24,'bold'))

        counter = 0
        while True:
            for z in screen.turtles():
                z.fd(0.1)
                z.bounce_on_edge()
            counter += 1
            if counter == 3000:
                g.clear()
                g.setx(0)
                g.sety(-20)
                g.color('red')
                s = '本程序由Python海龟模块制作'
                g.write(s,align='center',font=('',16,'bold'))
                
                g.sety(-55)
                g.color('gray')
                s = '需要本程序源码的请加微信scratch8'
                g.write(s,align='center',font=('',18,'underline'))                
    
screen.onclick(clickevent)
screen.mainloop()
