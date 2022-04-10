"""
   真正的冒泡排序动态演示
"""
from sprites import *

width,height = 620,400
screen = Screen()
screen.bgcolor('black')
screen.setup(width,height)

dummy = Sprite(visible=False)
dummy.sety(80)
dummy.color('yellow')
dummy.write("冒泡排序动态演示",align='center',font=('楷体',32,'normal'))
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
    b.scale(scales[i])          # 缩小
    b.goto(cors[i])             # 坐标定位    
    b.show()    
    paolist.append(b)

screen.delay(10)
delay = 500
while True:
    有交换 = False
    for i in range(9):
        # 发现更大的数据则进行交换
        if datas[i] > datas[i+1]:
            d = datas[i]
            datas[i] = datas[i+1]
            datas[i+1] = d
            # 对泡泡进行交换
            pao = paolist[i]
            paolist[i] = paolist[i+1]
            paolist[i+1] = pao

            # 下面用滑行命令让泡泡到坐标
            x1,y1 = cors[i]
            x2,y2 = cors[i+1]
            x = (x1+x2)/2
            paolist[i].slide((x,(y1+ 60)),delay)
            paolist[i+1].slide(cors[i+1],delay)
            paolist[i].slide((x1,y1),delay)
                             
            有交换 = True
    if 有交换 == False:break
            
            
            
