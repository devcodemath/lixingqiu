"""请更改切片规则，让不同的海龟出列"""

from turtle import *

color_list = ['red','orange','yellow','green','cyan','blue','purple','brown','pink','white']
screen = Screen()
screen.delay(10)
screen.bgcolor("black")

t = Turtle(shape='turtle')
t.index = 0                     #新增自定义属性
t.color(color_list[0])          #这个做为索引为0的海龟，红色
t.penup()                       #抬笔
t.bk(300)                       #后退300
t.setheading(90)                #朝上

for i in range(1,10):           #让i从1迭代到9，共克隆9次海龟   
    w = t.clone()               #克隆一只海龟
    w.index = i                 #自定义属性index的值为i
    w.color(color_list[i])      #设定颜色
    w.setx(t.xcor() + i * 50)   #设置x坐标

all_turtles = screen.turtles()   #所有的海龟对象
print(len(all_turtles))

#some_turtles = all_turtles[::2]  #海龟，0,2,4,6,8
some_turtles = all_turtles[::3]  #海龟，0,3,6,9

for turtle in some_turtles:      #每只海龟
    turtle.pendown()             #落笔
    turtle.fd(40)                #前进40
    turtle.write(turtle.index )  #写自己的index值
    turtle.bk(20)                #后退20
    
x = Turtle(visible=False)        #用来写切片规则的海龟对象
x.color("white")                 #颜色为白色
x.penup()                        #抬笔
x.goto(-100,100)                 #定位
x.write("[::3]",font=(None,20,"normal")) #写字

screen.mainloop()
