"""
   急速返航.py
   这是一个躲避小游戏。
   太空火箭执行完任务后要返回地球。
   可是地球周围布满了太空垃圾，唉，都是人类自己造的孽啊。
   请按左右方向箭头，操作火箭避开垃圾，成功返航。
   本程序用到了爆炸函数，注意它有一个times参数，这是爆炸次数！
   本程序需要Python精灵模块v1.36版本支持。如果没有安装，请在cmd输入以下命令安装。   
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites  --upgrade
"""
from sprites import *                      # 从精灵模块导入所有命令
from pygame import mixer                   # 从pygame模块导入混音器

mixer.init()                               # 混音器初始化
deathsnd = mixer.Sound('res/DEATH.wav')    # 实例化死亡声效
mixer.music.load('res/未开始音乐.mp3')     # 加载音乐 
mixer.music.play(-1,0)                     # 循环播放音乐

lines = ['res/line1.png','res/line2.png','res/line3.png']

screen = Screen()                          # 生成屏幕对象
screen.setup(480,360)                      # 设置屏幕宽高
screen.title('急速返航_躲避游戏_李兴球博客')
screen.bgpic('res/星空.png')               # 设置屏幕背景图 

earth = Sprite('earth',pos=(0,380))         # 地球角色 
# endpic是最后要显示的图片
endpic = Sprite(['res/成功.png','res/失败.png'],
                visible=False,pos=(0,1000))

line = Sprite(lines,visible=False)          # 新建线条角色
dynamic_bgs = []
for _ in range(20):   
   b = line.clone()                         # 克隆一条背景线
   b.shapeindex(random.randint(0,2))        # 随机选择一个造型
   x = random.randint(-240,240)             # 生成x坐标
   y = random.randint(360,3600)             # 生成y坐标
   b.goto(x,y)                              # 到达这个x,y坐标
   dynamic_bgs.append(b)                    # 添加到列表中
   b.show()                                 # 显示
   
pics1 = ['rocket0.png','rocket1.png','rocket2.png']
rocket = Sprite(pics1,pos=(0,-130))

# 序幕阶段，火箭是不动的，背景自上而下移动
clock = Clock()                             # 新建时钟对象
for _ in range(600):                        # 重复200次
   rocket.nextshape()                       # 火箭下一个造型 
   for bg in dynamic_bgs:                   # 迭代背景表中的线条
       bg.addy(-50)                         # 线条往下移50个单位
       if bg.ycor() < -180:                 # 如果线条y坐标小于-180
          x = random.randint(-240,240)      # 生成一个x坐标
          y = random.randint(360,3600)      # 生成一个y坐标
          bg.goto(x,y)                      # 线条到这个坐标   
   screen.update()                          # 更新屏幕显示
   clock.tick(60)                           # 固定fps为60帧

[bg.remove() for bg in dynamic_bgs]         # 删除所有
mixer.music.stop()                          # 停止播放音乐
mixer.music.load('res/循环音乐.mp3')        # 加载音乐
mixer.music.play(-1,0)                      # 循环播放音乐

# 进入第二阶段,太空垃圾来了，需要按左右方向箭头操作它躲避
garbs = []
garbage = Sprite('garbage',visible=False,pos=(0,300))
for _ in range(30):
   g = garbage.clone()
   g.shapeindex(random.randint(0,2))
   x = random.randint(-240,240)
   y = random.randint(360,3600)   
   g.goto(x,y)
   garbs.append(g)
   g.show() 
counter = 0

leftkey = Key("Left")
rightkey = Key("Right")
screen.listen()
isdead = False                      # 描述是否碰到太空垃圾的变量
for _ in range(2000):
   rocket.nextshape()
   if leftkey.down():rocket.addx(-4)
   if rightkey.down():rocket.addx(4)
   if rocket.overlap_with(garbs):
       rocket.hide()
       isdead = True
       break
   for g in garbs:
       g.addy(-6)
       if g.ycor() < -180:
          g.goto(random.randint(-240,240),
                 random.randint(360,3600))
   screen.update()
   clock.tick(60)

# 第三阶段,根据火箭是否爆炸决定显示什么
mixer.music.stop()
mixer.music.load('res/结束音乐.mp3')
mixer.music.play(-1,0)
endpic.home()
if isdead:    
    explode(rocket.pos(),
            ['res/爆炸0.png','res/爆炸1.png'],
            interval=150,times=5)
    deathsnd.play()
    endpic.shapeindex(1)
    endpic.wait(1)
    endpic.show()
else:
    # 首先删除所有垃圾，然后显示地球越来越大
    [g.remove() for g in garbs]
    rocket.setx(0)    
    s = 0.1
    earth.scale(s)
    for i in range(300):
        if i % 20 == 0 :
          earth.nextcostume()
        s = s + 0.004
        earth.scale(s)
        earth.addy(-1)
    endpic.shapeindex(0)
    endpic.wait(1) 
    endpic.show()
screen.mainloop()
