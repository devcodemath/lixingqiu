"""海底小纵小动画.py
,巴克队长出发动画.请用for或while循环实现这个动画。"""
 
from turtle import *
from time import sleep  

width,height=480,360
screen = Screen()
screen.setup(480,360)
screen.title("巴克队长,出发!")

图形表=[]

#列表的添加方法
for i in range(9):
    文件名 = "巴克队长出发-" + str(i) + ".png"
    图形表.append(文件名)
 

index=0                           #索引从0开始轮换
def changebg():
    global index
    screen.bgpic(图形表[index])   #显示索引为index的背景
    index=index+1
    index=index % 9
    screen.ontimer(changebg,100)  #100豪秒后自动调用 切换背景 函数
    
changebg()                        #调用切换背景函数
print("程序没有运行完毕,背景在不断切换中")
screen.mainloop()

 
