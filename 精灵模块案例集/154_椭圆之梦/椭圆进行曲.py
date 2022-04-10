"""
   椭圆之梦.py
   椭圆有什么梦想呢？运行下程序就知道了
   本程序会随机在屏幕上画椭圆。
   这些椭圆大小不一，颜色不一样，
   斜度也不一样，边框厚度也不一样。
   本程序有轻快的适于此动画的配音。
   给程序配音也是要花时间的哦，所以虽然程序或许简单，
   但它背后一样有付出，莫道君行早，还有早行人。
"""

from sprites import *           # 从精灵模块导入所有命令

screen = Screen()               # 新建屏幕对象
screen.tracer(0)                # 关闭自动刷新
screen.bgcolor('black')         # 设定背景为黑色
screen.title('椭圆之梦')        # 设定窗口标题

PlaySound('胡伟立 - 轻快.wav',SND_ASYNC|SND_LOOP)

bug = Sprite(visible=False)     # 新建虫子角色
bug.color('white')
bug.write('椭圆之梦',align='center',font=('',32,'bold underline'))
bug.wait(2)
counter = 0                     # 计数器
while True:    
    bug.randompos()             # 移到随机位置
    bug.randomcolor()           # 设定随机颜色
    bug.randomheading()         # 设定随机方向
    w = random.randint(1,5)     # 生成从1到5的w
    bug.pensize(w)              # 设定画笔粗细
    a = random.randint(10,100)  # 生成从10到100的a
    b = random.randint(10,100)  # 生成从10到100的b  
    bug.oval(a,b)               # 画椭圆形，长半轴为a,短半轴为b
    bug.wait(0.05)              # 等待0.05秒
    counter += 1                # 计数器加1
    

