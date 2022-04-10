from turtle import *

import colorsys
def coloradd(color,dh):
    """颜色增加
        color是三元组,分别为0-255的值.此函数把颜色转换成hls模式,对h进行增加dh的操作
       然后转换回去,dh是小于1的浮点数.
    """
    if len(color)==3 :
        h,l,s, = colorsys.rgb_to_hls(color[0]/255,color[1]/255,color[2]/255)
        h =  h + dh
        r,g,b = colorsys.hls_to_rgb(h,l,s)
        return int(r*255),int(g*255),int(b*255)
    else:
        return color
addcolor = coloradd   #定义别名

def colorset(color):
    """设定颜色,color范围为1到360"""
    color = color % 360
    color = color / 360.0    
    r,g,b = colorsys.hsv_to_rgb(color,1.0,1.0)
    
    return int(r*255),int(g*255),int(b*255)
    
setcolor = colorset    #定义别名

class Drawturtle(Turtle):
    yanse = (255,0,0)
    def __init__(self,shape = "turtle",visible = True,undobuffersize = 1000):
        Turtle.__init__(self,shape = shape,visible = visible,undobuffersize = undobuffersize)
        if self.screen.colormode()!=255:self.screen.colormode(255)
        self.pencolor(Drawturtle.yanse)
        
    def draw_polygon(self,number,length):
        """画正多边形，number边数，length,边长"""        
        
        for i in range(number):
            self.fd(length)
            self.rt(360/number)
            Drawturtle.yanse = addcolor(Drawturtle.yanse,0.01)
            self.pencolor(Drawturtle.yanse)
            
    def draw_sun(self,diameter,number,length):
        """画太阳，直径，number边数，length,边长"""        
        self.penup()
        for i in range(number):            
            self.fd(length/2)
            self.pendown()
            self.fd(length/2)
            self.penup()
            self.bk(length)
            self.rt(360/number)
            Drawturtle.yanse = addcolor(Drawturtle.yanse,0.1)
            self.pencolor(Drawturtle.yanse)
        self.dot(diameter)
    
    def draw_star(self,length):
        """画星星，length,边长"""        
  
        for i in range(5):     
            self.fd(length)  
            self.rt(144)
            Drawturtle.yanse = addcolor(Drawturtle.yanse,0.1)
            self.pencolor(Drawturtle.yanse)
    def draw8(self,step):
        
        for i in range(20):     
            self.fd(step)  
            self.lt(9)
            Drawturtle.yanse = addcolor(Drawturtle.yanse,0.01)
            self.pencolor(Drawturtle.yanse)
        for i in range(40):     
            self.fd(step)  
            self.rt(9)
            Drawturtle.yanse = addcolor(Drawturtle.yanse,0.01)
            self.pencolor(Drawturtle.yanse)
        for i in range(20):     
            self.fd(step)  
            self.lt(9)
            Drawturtle.yanse = addcolor(Drawturtle.yanse,0.01)
            self.pencolor(Drawturtle.yanse)
        
  

if __name__ == "__main__":     
    from random import randint
    t = Drawturtle()
    t.setundobuffer(3000)
    t.screen.setup(640,480)
    t.screen.colormode(255)
    t.screen.bgcolor("black")
    t.pensize(3)
    t.screen.delay(2)
    t.setheading(180)
    for i in range(10):
        t.draw8(5)
        t.right(36)
        
 
    while t.undobufferentries(): 
        t.undo()

        

        
