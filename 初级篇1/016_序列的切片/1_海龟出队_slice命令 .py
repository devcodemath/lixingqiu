"""请更改切片规则，让不同的海龟出列"""

from turtle import *


color_list = ['red','orange','yellow','green','cyan','blue','purple','brown','pink','white']
regulation = ((0,6,2),(1,10,3),(3,6,2),(-1,0,-1),(-2,4,-1))        # 元组形式的切片规则，给slice用
regulation2 = [ ":".join(str(x) for x in r) for r in regulation]   # 中括号形式的规则，如[1:5:2]

screen = Screen()
screen.delay(10)
screen.bgcolor("black")

"共生成10只海龟，第一只是本体，其它的是克隆体"
t = Turtle(shape='turtle')
t.index = 0                         #新增自定义属性
t.color(color_list[0])              #这个做为索引为0的海龟，红色
t.penup()                           #抬笔
t.bk(300)                           #后退300
t.setheading(90)                    #朝上
t.initcors = t.position()           #记录自己的初始坐标

for i in range(1,10):               #让i从1迭代到9，共克隆9次海龟   
    w = t.clone()                   #克隆一只海龟
    w.index = i                     #自定义属性index的值为i
    w.color(color_list[i])          #设定颜色
    w.setx(t.xcor() + i * 50)       #设置x坐标
    w.initcors = w.position()       #记录自己的初始坐标
    
"rose是用来写字的海龟"
rose = Turtle(visible=False)        #用来写切片规则的海龟对象
rose.color("white")                 #颜色为白色
rose.penup()                        #抬笔
rose.goto(-260,200)
rose.write("slice与切片演示动画",font=(None,32,"normal"))  #显示标题
rose.goto(-260,100)                 #定位

screen.turtles().pop()              #把 rose 对象弹出，它没必要在这个列表中。
all_turtles = screen.turtles()      #所有的海龟对象，有只默认的海龟也在内。
reg_amounts = len(regulation)       #规则数量

regindex = 0
def change(x,y):
    """单击屏幕，调用此函数，根据相应的取数规则显示相应的动画与文字"""
    
    global regindex
    
    for turtle in all_turtles:
        turtle.clear()
        turtle.goto(turtle.initcors)
        
    reg = regulation[regindex]       #取规则,slice形式的
    reg2 = regulation2[regindex]     #取规则，中括号形式的
     
    some_turtles = all_turtles[slice(*reg)]  #海龟 ，解包，some_turtles就是出队的海龟

    for turtle in some_turtles:      #每只海龟
        turtle.pendown()             #落笔
        turtle.fd(40)                #前进40
        turtle.write(turtle.index )  #写自己的index值
        turtle.bk(20)                #后退20
        
    rose.clear()
    s = "slice" + str(reg) + " --> [" + str(reg2) + "]" 
    rose.write( s ,font=(None,20,"normal")) #写字
    
    regindex = regindex + 1           #指向下一条规则
    regindex = regindex % reg_amounts #取余，这样它的值就不会超过总数
    print(regindex)    

screen.onclick(change)

screen.mainloop()
