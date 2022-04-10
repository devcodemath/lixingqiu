"""
   雪的梦幻.py
   本课主要学习如何自定义角色的多边形造型。
   屏幕的getshapes命令能获取所有的多边形造型。
   也可以用角色画一个形状，然后把这个形状设为角色的造型。
"""
from sprites import *                       # 从精灵模块导入所有命令

screen = Screen()                           # 新建屏幕
screen.bgcolor('dodger blue')               # 设定背景色
screen.setup(480,360)                       # 设定屏幕宽高
screen.bgpic('雪背景.png')                  # 设定背景图
screen.titlebar(False)                      # 去掉标题栏
screen.draggable()                          # 按中键可拖动
screen.addpopup()                           # 增加右键菜单  

t = Sprite(visible=False)                   # 新建不可见角色
t.color('white')                            # 设定颜色为白色

t.begin_poly()                              # 开始记录顶点
for x in range(8):                          # 在范围8迭代变量x
    t.fd(10)                                # 前进10个单位
    t.bk(10)                                # 倒退10个单位
    t.rt(45)                                # 右转45度
t.end_poly()                                # 结束记录顶点

p = t.get_poly()                            # 获取所有顶点坐标 
screen.addshape('snow',p)                   # 在形状列表中添加snow造型
t.shape('snow')                             # 设定t为snow造型
t.scale(0.3)                                # 设为0.3倍大小

for z in range(400):                        # 在范围200迭代z变量            
    x = random.randint(-240,240)            # 设定x坐标
    y = random.randint(200,1000)            # 设定y坐标
    t.goto(x,y)                             # 定位到x,y坐标
    t.stamp()                               # 盖图章

PlaySound('雪的梦幻.wav',SND_ASYNC|SND_LOOP)# 循环异步播放音乐 
while True:                                 # 当成立的时候 
    for item in t.stampItems:               # 对于每一个图章编号    
        t.movestamp(item,0,-0.1)            # 移动图章
        x,y = t.stampcors(item)             # 获取图章坐标
        if y < -180:                        # 如果y小于-180
           x = random.randint(-240,240)     # 设定x坐标
           y = random.randint(200,1000)     # 设定y坐标
           t.stampgoto(item,(x,y))          # 定位图章到x,y坐标
    screen.update()                         # 更新屏幕显示
    time.sleep(0.01)                        # 等待0.01秒 
            


