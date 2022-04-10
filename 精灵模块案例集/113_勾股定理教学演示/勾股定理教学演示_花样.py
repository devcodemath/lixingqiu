"""
   Python勾股定理粒子演示,本程序由sprites模块制作,请安装最新版本的sprites模块,要不然找不到相关方法.
"""
import math
from sprites import *

def spaceorwait():
    start = time.time()
    while not spacekey.down():
      if  time.time()-start>1:break
      screen.update()
def platlist(cors):
    """扁平化列表"""
    d = []
    for rows in cors:
        for x,y in rows:
            d.append((x,y))
    return d

def placeball(cors):
    stamps = []
    for rows in cors:        
        for x,y in rows:
            t.goto(x,y)
            sid = t.stamp()
            stamps.append(sid)
    return stamps

screen = Screen()
screen.bgcolor('dodger blue')
screen.title('勾股定理教学演示by李兴球')
screen.listen()
spacekey = Key('space')

ft = ('楷体',32,'normal')
ft2 = ('黑体',16,'normal')
w = Sprite(1,visible=False)
w.scale(0.4)
w.color('lime')
w.goto(0,240)
w.write('观看与思考',align='center',font=ft)
w.goto(0,210)
w.color('yellow')
w.write('这是演示什么定律',align='center',font=ft2)
w.goto(0,180)
w.color('cyan')
w.write('本程序用Python精灵模块制作',align='center',font=ft2)

t = Sprite(1,visible=False)
t.scale(0.4)
t.color('white')

initx,inity = -50,-100
while not spacekey.down():screen.update()

t.play('Crashteroids.wav',loop=True)
while True:
    t.clear()
    t.goto(initx,inity)
    # 画6x6的格子
    t.right(180)
    acors = t.draw_grid3(6,6,20,20,True)
    # 注意返回的acors是下面这样的样子
    # [[((170.71,100.00), 14), ((241.42,170.71), 15)],
    #  [((241.42,29.29),16), ((312.13,100.00), 17)]]
     
    # 画8x8的格子
    t.right(180)
    bcors = t.draw_grid3(8,8,20,20,True)

    # 画10x10的格子
    t.left(90)
    t.fd(120)
    angle = 90 - math.degrees(math.atan2(8,6))
    t.right(angle)
    ccors = t.draw_grid3(10,10,20,20)
    # 回到初始点
    t.left(angle)
    t.bk(120)
    t.right(90)
    
    dests = platlist(ccors)        # 扁平化列表
    t.wait(1)
    spaceorwait()                  # 按空格键或让它自己过去 
    # 把6x6格子里的小球移到10x10格子
    i = 0
    for rows in acors:
        for item in rows:
            destx,desty = dests[i]
            sid = item[1]                       # item[0]保存的是坐标,item[1]存图章编号
            t.stampslide(sid,(destx,desty),100)          
            i = i + 1
            
    # 继续把8x8格子里的小球移到10x10格子
    j = 0   
    for rows in bcors:
        for item in rows:
            destx,desty = dests[i]
            sid = item[1]          
            t.stampslide(sid,(destx,desty),100)
            i = i + 1
            j = j + 1
    print('再按空格键,所有小球回到小格')
    spaceorwait()                                # 按空格键或让它自己过去

    # 把后面的64个小球移回到当初的坐标
    for rows in bcors[::-1]:
        for item in rows[::-1]:
            destx,desty = item[0]                # 这是它当初的坐标
            sid = item[1]          
            t.stampslide(sid,(destx,desty),100)
    # 把后面的36个小球移回到当初的坐标
    for rows in acors[::-1]:
        for item in rows[::-1]:
            destx,desty = item[0]    # 这是它当初的坐标
            sid = item[1]          
            t.stampslide(sid,(destx,desty),100)
    initx += 0
    t.right(90)
    

print('程序结束')

