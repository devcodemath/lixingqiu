"""
   问卷调查器
   本程序演示做一个答题器。在sprites模块中，生成的窗口可以被分区。
   本程序的窗口分为上和下区。上面的框架叫topframe，下面的框架叫bottomframe。
   它们的master都是root。
   
   角色所在的滚动画布的master框架为displayframe，它在topframe框架中的左面。
   rightframe在topframe框架的右面。也就是说rightframe和displayframe的master都是topframe。
   读者可在rightframe和bottomframe中放置组件。
"""
from sprites import *

q1 = ['你最喜欢的职业是什么？',
      'A、教师',
      'B、律师',
      'C、自由职业',
      'D、企业家']
q2 = ['你喜欢一个人会有什么表现？',
      'A、总想着那个人',
      'B、天天看那个人的朋友圈',
      'C、总想着见面',
      'D、舍得付出']
q3 = ['你的理想是什么？',
      'A、科学家',
      'B、工程师',
      'C、政治家',
      'D、教育家']
q4 = ['如果你身体处于亚健康状态，会如何调理？',
      'A、少操心',
      'B、少食多餐，饮食均衡',
      'C、生活有规律',
      'D、不熬夜']
q5 = ['你向往什么样的生活？',
      'A、悠闲的田园生活',
      'B、快节奏的城市生活',
      'C、花天酒地的生活',
      'D、风花雪夜的生活']
questions = [q1,q2,q3,q4,q5]

answers = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
def sendanswer():
    """问卷调查结束后，把答案发送，也可以提交到网络哦！这里只是简单用showinfo显示一下"""
    info = ''
    for _ in answers:
        info = info + str(_) + "\n"
    filename = username + '的回答.txt'
    # 需要对filename进行过滤，去掉?,\,/,',""等字符
    #f = open(username + '的回答.txt',mode='w')
    #f.write(info)
    #f.close()
    screen.update()
    #os.system(filename)    
    showinfo("恭喜","你的回答已经成功发送到老师怀里了。")
    
def displayquestion(index):
    bug.clear()
    # 首先显示title
    info = 'No ' + str(index+1) + "：" + questions[index][0]
    bug.goto(0,120)
    bug.write(info,align='center',font=('楷体',18,'normal'))
    bug.goto(-150,50)
    for i in range(1,5):
        info = questions[index][i]
        bug.write(info,font=('楷体',14,'normal'))
        bug.addy(-50)        
    
def previousquestion():
    """回到上一题"""
    global index
    if index > 0:
       index -= 1
       displayquestion(index)
       for i in range(4):           
           value = answers[index][i]
           checkvars[i].set(value)  
           

def nextquestion():
    """到下一题"""
    global index
    if index < len(questions):
       # 首先收集当前答案信息到answers列表
       for i in range(4):
          value = checkvars[i].get()
          answers[index][i] = value
       
       # 然后显示下一题 
       index += 1
       if index == len(questions):
           bug.clear()
           bug.goto(0,100)
           bug.color('magenta')
           bug.write('Congratulations',align='center',font=('楷体',28,'normal'))
           bug.color('black')
           bug.goto(0,50)
           bug.write('问卷调查完毕！',align='center',font=('楷体',18,'normal'))
           bug.addy(-50)
           bug.write('请按下面的提交按钮',align='center',font=('楷体',18,'normal'))
           bug.addy(-50)
           bug.write('把答案发送给老师',align='center',font=('楷体',18,'normal'))
           
           # 销毁上一题，复选框和下一题按钮
           previousframe.destroy()
           checkframe.destroy()
           nextframe.destroy()
           b = TK.Button(root.bottomframe,text='   提  交   ',command=sendanswer,font=('楷体',28,'normal'))
           b.pack()
           
       else:
          displayquestion(index)
          # 把状态显示出来
          for i in range(4):           
            value = answers[index][i]
            checkvars[i].set(value) 
       

screen = Screen(3)         # 上下分区模式
screen.setup(540,480)
screen.bgcolor('cyan')
screen.title('问卷调查器')
root= screen._root
root.config(bg='#0099aa')
root.rightframe.pack_forget()
root.bottomframe.config(bg='#829684',padx=10,pady=10)
root.bottomframe.pack_forget()
username = screen.textinput('姓名','请输入姓名：')

bug = Sprite(visible=False)
bug.sety(100)
bug.color('magenta')
info = '问 卷 小 调 查'
bug.write(info,align='center',font=('微软雅黑',20,'normal'))
bug.sety(-100)
bug.color('green')
info = f'亲爱的朋友，你好，\n将对你进行一些小调查。\n'
info = info + f'本次调查共有{len(questions)}题，\n请认真在复选框中进行选择。\n按空格键开始答题。'
bug.write(info,align='center',font=('新宋体',14,'normal'))

spacekey = Key('space')
screen.listen()
while not spacekey.down():screen.update()

index = 0
displayquestion(index)                       # 显示第一道题

root.bottomframe.pack(expand=0)
previousframe = TK.Frame(root.bottomframe,bg='#0099ee')
previousframe.pack(side=TK.LEFT)
checkframe = TK.Frame(root.bottomframe,bg='#ffee99')
checkframe.pack(side=TK.LEFT,expand=1)
nextframe = TK.Frame(root.bottomframe,bg='#0099ee')
nextframe.pack(side=TK.RIGHT)

b1 = TK.Button(previousframe,text='上一题',font=('黑体',13,'normal'),command=previousquestion,padx=10,pady=10)
b1.pack()

checkvars = [TK.IntVar() for _ in range(4)]
for i in range(4):
    ck = TK.Checkbutton(checkframe,bg='#f0f0f0',text=chr(65+i),variable=checkvars[i],padx=10,pady=10)
    ck.pack(side=TK.LEFT)

b2 = TK.Button(nextframe,text='下一题',font=('黑体',13,'normal'),command=nextquestion,padx=10,pady=10)
b2.pack()

screen.mainloop()

