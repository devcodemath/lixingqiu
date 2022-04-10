"""
   幸运大转盘.py
   本程序画一个圆盘，在圆盘上写一些字，
   通过按空格键旋转饼状图，从而得到动画效果。
"""
from sprites import *

radius = 200                          # 定义半径
screen = Screen()                     # 新建屏幕
screen.tracer(0)                      # 关闭自动刷新
screen.title('幸运大转盘')            # 设定屏幕所在窗口标题

c = Sprite(visible=False)
c.color('light blue','orange')        # 画笔颜色和填充颜色 
c.pensize(4)                          # 画笔粗细为4
c.fd(radius)                          # 前进radius
c.left(90)                            # 左转90度 
c.pendown()                           # 落笔
c.begin_fill()                        # 开始填充 
c.circle(radius)                      # 画圆形
c.end_fill()                          # 结束填充
c.penup()                             # 抬笔
c.right(90)                           # 右转90度
c.bk(radius)                          # 倒退radius  

c.pendown()
c.color('light blue')
for _ in range(8):                    # 在范围8迭代_
    c.fd(radius)                      # 前进radius
    c.bk(radius)                      # 倒退radius
    c.rt(45)                          # 右转45度
c.penup()
c.update()                            # 更新显示

string = ['    你请我吃饭','    我请你吃饭',
          '    得到100元红包','    我们一起飞',
          '    你得到了幸福','    我得到了你',
          '    明天要下雨','    我们都会一生平安']
witems = []                                # 存储所有字的编号列表
w = Sprite(visible=False)
w.color('white')
heading = 0
for s in string:
    item  = w.write(s,angle=heading)       # 在底盘写字,朝向角度为heading
    witems.append(item)                    # 字的编号列表
    heading += 45                          # 角度增加45

bug = Sprite(visible=False)
bug.color('blue','red')
bug.arc(radius,0,45)
begin1 = 0                                 # 起始角
def rotate():
    """
       本函数让画饼状图的起始角start不断地以45度增加,
       而每次都是画固定角度的饼状图,通过不断地擦除与重画,
       我们就能看到旋转的饼状图动画。
    """
    global begin1
    screen.onkeypress(None,'space')        # 防止再次按空格键,这里取消和空格键的绑定
    begin2 = random.randint(720,2160)      # 需要旋转的角度的最大范围
    for start in range(begin1,begin2,45):  # 在begin1到begin2的范围迭代start
        bug.clear()                        # 擦除以前画的
        item = bug.arc(radius,start,45)    # 起始角为start,角度为45度的饼状图
        bug.wait(0.05)                     # 等待0.05秒
    start = start  % 360                   # 对360求余
    begin1 = start                         # 下次从这个角度开始旋转 
    screen.onkeypress(rotate,'space')      # 重新绑定空格键到rotate函数
    # 把字抬高,以便在最上面显示
    index = start//45                      # 整除45，求出每行字的索引号
    item = witems[index]                   # 取索引为index的项目编号
    screen.cv.tag_raise(item)              # 通过画布的tag_raise命令抬升这个项目
    
screen.onkeypress(rotate,'space')
screen.listen()                            # 监听屏幕按键
screen.mainloop()                          # 进入屏幕主循环



