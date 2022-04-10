"""
   阅读程序，回答以下问题：
   1、程序中有几个列表？ 答：两个表,分别是funcs表和names表.
   2、每个函数返回什么值？ 答；返回return后面的字符串。
   3、写出程序的运行结果。 答：运行本程序即可。
   4、请导入海龟模块，把每个同学的爱好一行一行地写在海龟画图屏幕上。
      格式为：胡学琴的爱好是：我的爱好是逛街
      答：见以下代码。
""" 

def func1():
    return "我喜欢吃东西。"
    
def func2():
    return "我爱学习。"

def func3():
    return "我最喜欢爬山." 
    
def func4():
    return "我的爱好是逛街。"
    
def func5():
    return "看大片是我的爱好。" 

funcs = [func1,func2,func3,func4,func5]
          
hobbys = {'胡学琴':funcs[3],'赵紫阳':funcs[0],'张美美':funcs[2],'李雪花':funcs[1],'钱咪咪':funcs[4]}

names = list(hobbys.keys())
names.reverse()

for name in names:
    print(hobbys[name]())

"以下是问题4的答案"
from turtle import *

t = Turtle(visible=False )
t.penup()
t.goto(-240,100)
for key in hobbys:
    info = key + "的爱好是：" + hobbys[key]()
    t.write(info,align='left',font=(None,22,'normal'))
    t.sety(t.ycor() - 50)
t.screen.exitonclick()












