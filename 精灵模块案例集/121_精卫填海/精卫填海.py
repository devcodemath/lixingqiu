"""
   精卫填海.py
   本程序不断地按顺序把列表中的图像设为屏幕的背景图,
   精卫鸟会不断地从屏幕左边出来,有时候会扔石头。
"""
from random import randint              # 从随机模块导入randint命令
from time import sleep                  # 从时间模块导入sleep命令
from sprites import *                   # 从精灵模块导入所有命令

def throwstone():
    """
       设定一定的机率,让小鸟扔石头的函数
    """
    if stone.ishide():                  # 如果石头是隐藏的 
        if randint(1,100)==1:           # 设定一定的概率
            stone.goto(bird.pos())      # 石头到鸟的坐标
            stone.show()                # 显示石头
    else:                               # 否则(石头就是显示的)
        stone.addy(-5)                  # 往下移动5个单位
        if stone.ycor()<-100:           # 如果石关的y坐标小于-100 
            stone.hide()                # 隐藏石头        
        
screen = Screen()                       # 新建屏幕
screen.setup(490,360)                   # 设定屏幕宽高 
screen.titlebar(False)                  # 关闭标题栏
screen.draggable()                      # 按鼠标中键拖动窗口
screen.bgcolor('black')                 # 设定背景为黑色 
screen.addpopup()                       # 加上右键菜单

images = []                             # 新建名为images列表,它的内容将是所有的背景图片
for i in range(100):                    # 由于frames文件夹下有从0.png到99.png的100张图片
    filename = os.getcwd() + os.sep + 'frames' + os.sep + str(i) + ".png"
    images.append(filename)             # 把文件添加到列表

stone = Sprite(shape='石头.png',visible=False)
stone.scale(0.5)                        # 设为原来一半大小
stone.setalpha(128)                     # 设置半透明

# 新建隐藏的小鸟角色,它用来代表精卫鸟
bird = Sprite(shape='精卫鸟小.png',pos=(0,50),visible=False) 
bird.play('精卫填海.wav',loop=True)     # 循环播放
bird.write("精卫填海",align='center',font=("楷体",24,'bold'))
bird.goto(-300,100)                     # 定位到坐标(-300,100)
bird.show()                             # 显示出来 

index = 0                               # 新建变量,初始值为0
while True:                             # 当成立的时候
    bird.fd(2)                          # 前进2个单位的距离
    if bird.xcor()>245:bird.setx(-300)  # 如果x坐标大于245,则设置x坐标为-300
    throwstone()                        # 扔石头
    screen.bgpic(images[index])         # 设定屏幕背景图片
    screen.update()                     # 刷新屏幕显示
    index = index + 1                   # index的值增加1
    index = index % 100                 # 索引对100求余数
    sleep(0.1)                          # 等待0.1秒
