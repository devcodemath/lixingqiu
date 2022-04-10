"""
    竹林弹字游戏.py
    本程序会把汉字转换一些圆形图片,然后从屏幕底部弹出来。
    这个程序有两个线程，每个线程都是一个死循环。
    操作方法为单击汉字，汉字就会爆炸，当然加上语音朗读功能就更好啦。
    本游戏需要Python精灵模块支持，如果你的电脑没有安装，请用cmd命令打开管理员窗口，输入以下命令：
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites  --upgrade
    本程序的音乐也配的很好哦，请自行加上语音郎读功能，从而变成一个有趣的汉字学习小程序。
"""
from sprites import *
from threading import Thread

def makergbcolors(n=128):        
    """产生颜色表，饱和度和亮度最高，所以很鲜艳"""
    cs = []
    for y in range(n):
        x = random.random()
        r,g,b = colorsys.hsv_to_rgb(x,1,1)
        r,g,b = int(r*255),int(g*255),int(b*255)
        cs.append((r,g,b))    
    cs = list(set(cs))
    return cs

cs = makergbcolors()

def make_image(char):
    """生成圆形含字图形对象"""
    color = random.choice(cs)
    color_rev = ((255-color[0]),(255-color[1]),(255-color[2]))
    myfont = ImageFont.truetype("msyh.ttf", 60)
    cm = Image.new("RGBA",(100,100))
    draw = ImageDraw.Draw(cm)
    fontsize = draw.textsize(char,font = myfont)     # 文字的宽度和高度
    draw.ellipse((0,0,99,99),fill=color,width=5)
    x = 50 - fontsize[0]//2
    y = 50 - fontsize[1]//2
    draw.text((x,y),char,fill=color_rev,font=myfont)
    return cm                                        # 返回图形对象

s = '我爱伟大的中华人民共和国它是一个非常伟大的国家我们一定要爱不释手'
s = set(s)
costumes = {}                                  # 造型名称和汉字的字典
for char in s:
    im =  make_image(char)
    filename = 'res/' + char + ".png"
    costumes[filename] = char
    im.save(filename)

exp = ['res/explosion0.png','res/explosion1.png']
width,height = 626,481
screen = Screen()
screen.bgpic('bamboo.jpg')
screen.setup(width,height)
screen.title('竹林弹字游戏by李兴球')

k = Mouse()                                    # 鼠标左键

def run1():
    c = Sprite(shape=list(costumes.keys()),pos=(0,100-height//2))
    clock = Clock()
    while True:
        c.dx = random.randint(-10,10)
        c.dy = random.randint(15,30)
        c.dist = 0
        shapename = c.randomshape()              # 返回造型名称
        char = costumes[shapename]               # 汉字        
        while True:
            if c.dist > 110 and c.collide_edge():break
            if k.down() and c.collide_mouse():
                explode(c.pos(),exp)
                break
            c.addx(c.dx)
            c.addy(c.dy)
            c.dy -= 1
            c.dist += 1
            clock.tick(30)
        c.hide()
        c.goto(0,100-height//2)
        c.show()

thread1 = Thread(target=run1)
thread1.start()


def run2():
    c = Sprite(shape=list(costumes.keys()),pos=(0,100-height//2))
    clock = Clock()
    while True:
        c.dx = random.randint(-10,10)
        c.dy = random.randint(15,30)
        c.dist = 0
        shapename = c.randomshape()              # 返回造型名称
        char = costumes[shapename]               # 汉字        
        while True:
            if c.dist > 110 and c.collide_edge():break
            if k.down() and c.collide_mouse():
                explode(c.pos(),exp)
                break
            c.addx(c.dx)
            c.addy(c.dy)
            c.dy -= 1
            c.dist += 1
            clock.tick(30)
        c.hide()
        c.goto(0,100-height//2)
        c.show()

thread2 = Thread(target=run2)
thread2.start()

PlaySound('Moon_in_the water.wav',SND_LOOP|SND_ASYNC)
screen.mainloop()






