"""
   单击抛物粒子效果
"""
from sprites import *          # 从精灵模块导入所有命令

def make_particle():
    """生成一个粒子"""
    p = Sprite(shape='circle',visible=False)
    p.da = -1                  # 加速度
    p.scale(0.2)               # 缩小 
    p.randomcolor()            # 设定为随机的颜色
    return p

def init_particles(x,y):
    """单击后对所有粒子重新设定水平和垂直速度"""
    [pa.goto(x,y) for pa in particles] # 每个粒子都到鼠标指针坐标
    for pa in particles:               # 每一颗粒子
        pa.dx = random.uniform(-5,5)   # 设定粒子的水平速度
        pa.dy = random.uniform(10,20)
        pa.show()

def particles_fall():
    """所有粒子在受到重力的情况下往下掉,直到碰撞到边缘"""
    counter = 0
    clock = Clock()
    while True:        
        for pa in particles:
            x = pa.xcor() + pa.dx
            y = pa.ycor() + pa.dy
            pa.dy = pa.dy + pa.da
            pa.goto(x,y)         # 定位到坐标x,y
            if pa.collide_edge():# 如果碰到边缘
                counter += 1     # 统计一下数量
                pa.hide()        # 到了边缘就隐藏 
        # 如果都隐藏了
        if counter == len(particles):
           break
        clock.tick(30)
        
def start_fall(x,y):
    """开始下落"""
    screen.onclick(None)        # 取消单击绑定    
    init_particles(x,y)         # 重新设定所有粒子的水平和垂直速度         
    particles_fall()            # 所有粒子往下掉
    screen.onclick(start_fall)  # 重新绑定鼠标左键单击事件到start_fall
    
screen = Screen()
screen.bgcolor('black')
screen.colormode(255)
# 生成25颗粒子
particles = [make_particle() for x in range(25)]
                
screen.onclick(start_fall)
screen.mainloop()    
