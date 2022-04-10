"""小女孩的舞蹈.py"""

from turtle import *
from winsound import PlaySound,SND_ASYNC,SND_LOOP

PlaySound("Cave.wav",SND_ASYNC|SND_LOOP)
背景表 = ["b0.png","b1.png","b2.png","b3.png","b4.png","b5.png","b6.png","b7.png"]
bgamount = len(背景表)                   #背景数量
女孩表 = ["girl0.gif","girl1.gif","girl2.gif","girl3.gif"]
gamount = len(女孩表)                    #女孩造型数量

s = Screen()
s.setup(480,360)
s.title("小女孩的舞蹈_python海龟画图版")

for item in 女孩表:            #每个图片都加到形状列表
    s.addshape(item)

index = 0
def 换背景():
    global index
    s.bgpic(背景表[index])
    index = index + 1
    index = index % bgamount
    s.ontimer(换背景,500)
换背景()

t = Turtle(shape = "girl0.gif")
i = 0
def 换造型():
    global i
    t.shape(女孩表[i])
    i =  i + 1
    i = i % gamount
    s.ontimer(换造型,450)
换造型()



s.mainloop()
