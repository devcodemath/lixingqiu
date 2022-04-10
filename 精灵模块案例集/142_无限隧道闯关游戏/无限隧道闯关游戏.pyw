"""
   无限隧道闯关游戏.py
   本程序演示一个按键操作的多关卡小游戏。
"""
from sprites import *                    # 从精灵模块导入所有命令

screen = Screen()                        # 新建屏幕
screen.setup(800,600)                    # 设定宽高
screen.bgcolor('black')                  # 背景为黑
screen.title('无限隧道闯关游戏')

level = 1                                # 关卡编号
ft = ('黑体',32,'normal')                # 新建字体样式
w = Sprite(visible=False)                # 用来写关卡号的角色
w.color('green')                         # 写字的颜色
w.goto(0,220)                            # 坐标定位

ball = Sprite(1)                         # 新建小球
ball.bk(400)                             # 倒退400个单位

pen1 = Sprite(visible=False)             # 画笔1
pen1.width(4)                            # 画笔线宽(pensize)
pen1.color('red')                        # 画笔颜色
pen1.bk(400)                             # 倒退400个单位
pen1.addy(80)                            # y坐标增加80

pen2 = Sprite(visible=False)             # 画笔2
pen2.width(4)                            # 画笔线宽(pensize)
pen2.color('red')                        # 画笔颜色    
pen2.bk(400)                             # 倒退400个单位
pen2.addy(-80)                           # y坐标减小80

k = 1                                    # 移动速度的系数
leftkey = Key('Left')                    # 左方向箭头
rightkey = Key('Right')                  # 右方向箭头
upkey = Key('Up')                        # 上方向箭头
downkey = Key('Down')                    # 下方向箭头
screen.listen()                          # 监听屏幕按键
                              
while True:
    w.clear()                            # 清除所写的关卡号
    w.write(level,align='center',font=ft)
    dx = 0                               # 小球水平速度
    dy = 0                               # 小球垂直速度 
    pen1.down()                          # 笔1落笔
    pen2.down()                          # 笔2落笔
    while pen1.xcor() < 400:             # 当笔1的x坐标小于400
        if pen1.ycor() > 200 :           # 如果笔1的y坐标大于200
            fx = random.randint(-45,0)   # 方向为斜下方 
        elif pen2.ycor() < -200:         # 如果笔2的y坐标小于-200
            fx = random.randint(0,45)    # 方向为斜上方  
        else:
            fx = random.randint(-45,45)  # 否则方向为-45到45度之间
        di = random.randint(10,100)      # 设定随机移动的距离
        pen1.setheading(fx)              # 设定笔1的方向
        pen1.fd(di)                      # 前进di的距离
        pen2.setheading(fx)              # 设定笔2的方向 
        pen2.fd(di)                      # 前进di的距离
    pen1.up()                            # 笔1抬笔
    pen2.up()                            # 笔2抬笔

    running = True
    while running and ball.xcor()<380:   # 球的x坐标小于380并且running为真
        x = ball.xcor() + dx
        y = ball.ycor() + dy
        ball.goto(x,y)                   # 坐标定位
        if leftkey.down(): dx -= 0.05 * k
        if rightkey.down(): dx += 0.05 * k
        if upkey.down(): dy += 0.05 * k
        if downkey.down(): dy -= 0.05 * k
        
        r = ball.find_overlapping()      # 查找有无碰到红线
        if r:running = False             # 碰到了红线,r就不是空的      
        screen.update()                  # 更新屏幕显示 
        time.sleep(0.01)                 # 等待0.01秒
    if running == False:break            # 这里是退出最上层while

    # 小球到了最右边坐标后,准备下一关的代码    
    pen1.clear()                         # 笔1清空              
    pen2.clear()                         # 笔2清空  
    ball.setx(-400)                      # 球移到最左边
    pen1.setx(-400)                      # 笔1移到最左边
    pen2.setx(-400)                      # 笔2移到最左边
    k = k + 0.1                          # k增加了,让下一关更难
    level += 1                           # 关卡编号增加1
    
explosionframes = ['res/explosion0.png',
                   'res/explosion1.png']
ball.hide()
ball.play('EXPLO4.wav')                  # 播放爆炸声
explode(ball.pos(),explosionframes)      # 在球的坐标处显示爆炸效果

screen.mainloop()                        # 进入屏幕主循环
