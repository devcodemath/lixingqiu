"""
   勇闯黑暗迷宫,迷宫会停电,仅凭记忆去碰小花!
"""
from sprites import *
from winsound import PlaySound,SND_ASYNC

PlaySound('勇闯.wav',SND_ASYNC)
screen = Screen()
screen.setup(640,480)
screen.title('勇闯黑暗迷宫')        # 设定标题

ball = Sprite(1)                    # 新建小球角色
ball.color('black')
ball.bk(300)
ball.pensize(20)
ball.pendown()
ball.fd(400)
ball.penup()
ball.goto(0,250)
ball.pendown()
ball.goto(0,100)
ball.penup()

ball.goto(0,-250)
ball.pendown()
ball.goto(0,-100)
ball.penup()

ball.goto(160,100)
ball.pendown()
ball.goto(160,-100)
ball.penup()

ball.goto(-310,230)                      # 定位到这开始画黑色边框
ball.pendown() 
for _ in range(2):
    ball.fd(610)
    ball.rt(90)
    ball.fd(460)
    ball.rt(90)
ball.penup()

ball.goto(-200,-150)                      # 最终定位到这
ball.say('按方向箭头\n操作我碰到小花',10,False)

flower = Sprite('res/flower.png')        # 新建小花角色
flower.goto(-200,150)                    # 小花定位到这里

w = Sprite(visible=False)                # 写字的角色
w.goto(-100,30)                          # 定位到(-100,30)
info = "马上要停电,请立即记住迷宫布局"
ft = ('',23,'normal')
w.write(info)                            # 写提示信息
w.wait(4)                                # 等待4秒钟
w.goto(0,30)                             # 定位到(0,30)
# 下面是写倒计时3,2,1
for x in range(3):
    w.clear()    
    w.write(3-x,align='center',font=ft)
    w.wait(1)
w.clear()
screen.bgcolor('black')                 # 把背景设为黑色

leftkey = Key('Left')                   # 新建左方向箭头
rightkey = Key('Right')                 # 新建右方向箭头
upkey = Key('Up')                       # 新建上方向箭头
downkey = Key('Down')                   # 新建下方向箭头
screen.listen()                         # 监听屏幕按键 
flag = None
while True:
    if leftkey.down():ball.addx(-5)      # 按左键则往左移
    if rightkey.down():ball.addx(5)      # 按右键则往右移
    if upkey.down():ball.addy(5)         # 按上键则往上移
    if downkey.down():ball.addy(-5)      # 按下键则往下移
    if ball.collide(flower,0.5):         # 碰到花则闯关成功
        print('成功')
        flag = True
        break
    if ball.find_overlapping(flower):    # 碰到墙,(排除碰到花)则闯关失败！ 
        print('失败')
        flag = False
        break
    screen.update()
    time.sleep(0.01)

screen.bgcolor('white')                 # 设屏幕背景为白色
if flag: 
    w.write('成功',align='center',font=ft)
    PlaySound('鼓掌声.wav',SND_ASYNC)
else:
    w.write('失败',align='center',font=ft)
    PlaySound('命运交响曲.wav',SND_ASYNC)
screen.mainloop()







