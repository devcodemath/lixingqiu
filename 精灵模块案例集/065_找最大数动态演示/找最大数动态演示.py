"""
   找最大数动态演示
"""
from sprites import *

width,height = 620,400
screen = Screen()
screen.bgcolor('black')
screen.setup(width,height)

dummy = Sprite(visible=False)
dummy.sety(80)
dummy.color('yellow')
dummy.write("找最大数动态演示",align='center',font=('楷体',32,'normal'))
datas = [random.randint(50,220) for x in range(10)]
scales = [data/1000 for data in datas] # 每个泡泡的缩放比例

cors = []
x = -width//2 + 55              # 起始x坐标
y = -50                         # 起始y坐标
for _ in range(10):             # 生成10个坐标
    cors.append((x,y))          # 添加到坐标表
    x = x + 55                  # x坐标增加
    
paolist = []                    # 泡泡列表
for i in range(10):
    b = Sprite('pao.png',pos=cors[i],visible=False)
    b.saycolor('yellow')
    b.scale(scales[i])          # 缩小
    b.goto(cors[i])             # 坐标定位    
    b.show()    
    paolist.append(b)

screen.delay(10)
delay = 500

index = 0
max_data = datas[index]
for i in range(1,10):
    # 发现更大的数据则进行记录
    if datas[i] > max_data:
        max_data = datas[i]
        index = i
        paolist[index].say('我比前面的大',2)
    else:
        paolist[i].say('我小',2)

paolist[index].say('我最大',3000000)
            
            
            
