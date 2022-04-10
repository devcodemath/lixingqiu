"""
   沙漠打地鼠.py
"""
from sprites import *

width,height = 480,360
screen = Screen()
screen.bgpic('stage.png')
screen.setup(width,height)

# 六个坑位
cors = [(-105,-10),(25,-10),(165,-10),
        (-105,-90),(25,-90),(165,-90)]# 每只地鼠的坐标表
# 地鼠列表
dishu_list = [Sprite(shape='dishu.png',pos=cor,
               visible=False)  for cor in cors]

hammer = Sprite(shape='锤子1.png')    # 新建锤子
hammer.right(45)

m1 = Mouse()                          # 鼠标左键按键实例
counter = 0                           # 计数器

while True:
    hammer.goto(mouse_pos())          # 锤子跟随鼠标指针
    if m1.down() :
        hammer.shape('锤子2.png')     # 单击鼠标左键切换到此造型
    else:   
        hammer.shape('锤子1.png')     # 松开了则切换到此造型 

    # 随机出现一只地鼠
    if random.randint(1,500)== 1:
        ds = random.choice(dishu_list)
        if ds.isvisible():continue   # 如果本来就是显示的 
        ds.show(1)                   # 地鼠最多显示1秒 
        
    # 地鼠碰到锤子则进行统计并隐藏地鼠,以防止重复统计
    for dishu in dishu_list:
        if dishu.ishide():continue
        if dishu.collide(hammer) and m1.down():
            dishu.play('hand clap.wav')
            counter = counter + 1
            dishu.hide()             # 隐藏地鼠 
            explode(dishu,'爆炸.png')# 用一张图片表示爆炸效果
            screen.title(counter)

