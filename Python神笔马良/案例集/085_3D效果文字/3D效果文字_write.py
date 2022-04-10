"""
   3D效果文字_自定义方法版.py
   本程序给Turtle类新增了addx和addy方法，
   还增加了write3D这个方法，用来写3D效果文字
"""
import turtle

turtle.Turtle.addx = lambda self,dx:self.setx(self.xcor() + dx)
turtle.Turtle.addy = lambda self,dy:self.sety(self.ycor() + dy)

def _writex(self,string,bg='black',fg='blue',
            align='center',move=False,font=('',16,'normal')):
    """写具有3D效果的文字"""
    # 保存
    oldpencolor = self.pencolor()
    oldpos = self.position()
    olddown = self.isdown()
    oldspeed = self.speed()
    olddelay = self.screen.delay(0)
    self.screen.delay(0)
    self.speed(0)
    self.pencolor(bg)
    self.penup()
    
    self.addx(-2)
    self.addy(2)
    self.write(string,align=align,font=font,move=move)    
    
    self.addx(-2)
    self.addy(2)
    self.write(string,align=align,font=font,move=move)
    
    self.pencolor(fg)
    self.write(string,align=align,font=font,move=move)
    # 恢复
    self.pencolor(oldpencolor)
    self.goto(oldpos)
    self.speed(oldspeed)
    self.screen.delay(olddelay)
    if olddown:self.pendown()

turtle.Turtle.write3D = _writex
    
zt = ('微软雅黑',42,'normal')
string = '3D效果文字\n风火轮编程'

tom = turtle.Turtle(visible=False)
tom.penup()
tom.screen.bgcolor('yellow')
tom.write3D(string,font=zt)
tom.screen.mainloop()


