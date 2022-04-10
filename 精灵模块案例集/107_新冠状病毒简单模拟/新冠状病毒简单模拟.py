"""
  新冠状病毒疫情简单模拟程序，以下程序用
  红点表示已经感染的人，用绿点表示未感染的人，用白点表示医生
  本程序方案可以自行设置,让其出现不同的结果。
"""

from sprites import *

radius = 150                # 活动半径

red_amounts = 30            # 1、已感染的数量
red_speed_k = 5             # 2、红点移动速度因子

lime_amounts = 300         # 3、未感染人群数量
lime_protects = 300        # 4、有防护措施的数量
lime_speed_k = 0           # 5、未感染人的移动速度

white_amounts = 50          # 6、白衣天使数量
white_speed_k = 5           # 7、白衣天使移动速度

width,height = 500,500
screen = Screen()
screen.tracer(0,0)
screen.bgcolor('black')
screen.setup(width,height)
screen.title('新冠状病毒疫情简单模拟程序')
reds = [Sprite(shape='dot') for x in range(red_amounts)]
for p in reds:
    p.scale(2)
    p.set_tag('red')
    p.randomheading()
    p.speed = red_speed_k * random.randint(1,5)  # 重定义speed    
    p.gotorandom()
    while p.distance((0,0))>radius:
         p.gotorandom()
    p.color('red')

limes = [Sprite(shape='dot') for x in range(lime_amounts)]
counter = 0
for p in limes:
    p.scale(2)
    p.set_tag('lime')
    p.randomheading()
    p.speed = lime_speed_k * random.randint(1,5)
    p.protect = False          # 自定义属性
    if counter < lime_protects:
        p.protect = True       # 如果带了口罩,碰到红色粒子不会变成红色粒子
        counter = counter + 1   
    p.gotorandom()
    while p.distance((0,0))>radius:
         p.gotorandom()
    p.color('lime')

whites = [Sprite(shape='dot') for x in range(white_amounts)]
for p in whites:
    p.scale(2)
    p.set_tag('white')
    rr = random.choice(reds)  # 随机挑一名红色感染者，
    p.heading(rr)
    p.speed = white_speed_k * random.randint(1,5)    
    p.gotorandom()
    while p.distance((0,0))>radius:
         p.gotorandom()
    p.color('white')
screen.update()
running = True
while running:
    for r in reds[:]:
        if reds == []:break
        r.fd(r.speed)
        if r.collide_others('white'):  # 碰到医生
            r.color('lime')
            r.set_tag('lime')
            r.protect = True
            r.speed=0
            reds.remove(r)
            limes.append(r)
        r.update()    
        if r.distance((0,0)) > radius:r.right(180)
    for g in limes[:]:
        if reds == []:break
        g.fd(g.speed)
        if g.protect == False and g.collide_others('red'):
            g.color('red')
            g.set_tag('red')
            g.speed = red_speed_k * random.randint(1,5)
            limes.remove(g)
            reds.append(g)
        g.update()
        g.bounce_on_edge()
    for w in whites:
        if reds == []:break
        if random.randint(1,100) == 1:
           rr = random.choice(reds)  # 随机挑一名红色感染者，
           w.heading(rr)
        w.fd(w.speed)
        w.update()
        if w.distance((0,0)) > radius:w.right(180)
    if len(reds) == 0 :running = False

        
