"""
   烟花效果.py
   本程序会有一个彩色的小点从下往上升起,然后爆炸
   粒子效果是用图章实现的,注意精灵对象图章列表名字叫做:stampItems。
   程序中新建了一个字典，它以图章的编号为键，以图章的dx和dy为值存储数据。
   每个图章都受到重力的影响，它们的加速度都是-0.5。
"""
from sprites import *

def fire_rise():
    """烟花上升"""
    fire.randomcolor()         # 随机颜色
    fire.goto(0,-300)          # 坐标定位
    fire.dx = 0                # 水平速度
    fire.dy = 20               # 垂直速度
    fire.da = -0.5             # 加 速 度
    fire.show()                # 显示出来    
    while fire.dy >= 0:        # 当在上升的时候
        fire.move(fire.dx,fire.dy)
        fire.stamp(0.2)
        fire.dy = fire.dy + fire.da    
        clock.tick(60)
    fire.hide()
    fire.wait(0.2)             # 这里一定要至少等0.2,由于上面的图章要0.2秒才删除

def make_particles():
    """生成一定数量的图章(表示粒子),所有图章编号都存储在fire.stampItems列表中"""
    global speeds
    [fire.stamp() for _ in range(amounts)]
    speeds = {}    
    for x in range(amounts):
        dx = random.uniform(-5,5)
        dy = random.uniform(-5,5)
        st = fire.stampItems[x]      # speeds字典存储图章编号到[dx,dy]之间的映射
        speeds[st] = [dx,dy]         # 把水平速度和垂直速度存入字典

def particles_fall():
    """所有的粒子下落"""
    counter = 0    
    while counter < amounts:            
        for st in fire.stampItems:   # 遍历每颗粒子(图章编号)
            if st not in fire.stampItems:continue
            speeds[st][1] += - 0.2   # 垂直速度-0.2
            # 取出dx和dy,移动图章st
            fire.movestamp(st,speeds[st][0],speeds[st][1])
            x,y = fire.stampcors(st) # 获取每个图章的坐标
            if y < -height//2:
                fire.clearstamp(st)  # 清除达到下边界的粒子
                counter += 1         # 计数                                   
        screen.update()
        clock.tick(60)
        
width,height = 600,600
screen = Screen()
screen.bgcolor('black')

fire = Sprite(shape='circle',visible=False)
fire.scale(0.1)                      # 缩小为10%

# 存储每个图章速度的字典,键是图章编号,值是(dx,dy),即水平速度和垂直速度
speeds = {}
amounts = 250                  # 盖的图章的数量
clock = Clock()                # 新建时钟对象
while True:
    fire_rise()
    make_particles()
    particles_fall()  
    print('全部落完')

