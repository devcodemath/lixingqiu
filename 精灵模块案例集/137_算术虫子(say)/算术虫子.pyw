from sprites import *
from random import randint

s = 0
score = 0
screen = Screen()                        # 新建屏幕
screen.setup(800,600)                    # 设定屏幕宽高
screen.bgcolor('dodger blue') 
bug = Sprite()                           # 新建虫子角色
bug.left(90)                             # 虫子左转90度

def question():
    """每隔5秒运行一次的函数"""
    global s                             # 申明s为全局变量 
    a = randint(0,10)                    # 给a赋一个从0到10之间的数值
    b = randint(0,10)                    # 给b赋一个从0到10之间的数值
    s = randint(0,1)                     # s代表出正确的题目还是出错误的题目
    if s == 1 :                          # s为1表示显示正确的答案
        c = a + b
    else:                                # s为0表示显示错误的答案         
        c = randint(0,20)
        while c==(a+b):c = randint(0,20) # 这里是为了防止c刚好和a+b的和相等
    string = str(a) + "+" + str(b) + "=" + str(c)
    bug.gotorandom(-300,300,-200,200)    # -300是left,300是right,-200是bottom,200是top
    bug.show()                           # 显示虫子
    bug.say(string,5,False)              # 异步执行say命令,显示说话泡泡5秒
    screen.ontimer(question,5000)        # 5秒后再次调用question函数
question()                               # 调用一次question函数

def answer(x,y):
    """单击虫子后运行的函数"""
    global s,score                       # 申明s和score为全局变量
    if s == 1:score += 10                # 如果s是1,则加10分 
    bug.hide()                           # 隐藏角色 
    screen.title(str(score))             # 在标题栏显示得分

bug.onclick(answer)                      # 单击角色调用answer函数
screen.mainloop()                        # 进入主循环
 
