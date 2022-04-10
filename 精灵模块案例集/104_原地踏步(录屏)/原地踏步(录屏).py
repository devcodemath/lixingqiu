"""
   原地踏步(录屏).py
   本程序主要演示如何使用screen.save命令进行录屏，
   它会对当前窗口进行抓屏，所以在运行程序时不要把
   当前窗口遮住、移开或最小化，screen.save可以加文件名参数，
   写上文件名参数的话，由于会写文件到磁盘，会让程序运行速度变慢。
   也可以不加任何参数,这样它会返回图形对象,以便接下来的程序保存它。
   以下是save方法的定义原形：
   save(self,filename=None,size=None,margin=5,full=False):
   size是用来指定区域的，是一个四元组，margin为边距，full表示是否截全屏。
   本程序需要sprites模块支持,安装方法: pip install sprites
  
"""
from sprites import *

# 列表推导式,frames存储每张猫的造型帧图
frames = [f'cats/{i}.png' for i in range(16)]

screen = Screen()            # 新建屏幕
screen.setup(480,360)        # 设定宽高
screen.bgpic('res/sky.png')  # 背景图像

cat = Sprite(shape=frames)   # 新建小猫角色

frames = []                  # 重定义frames，用于保存每一帧
for x in range(10):          # 重复执行10次
    cat.nextcostume()        # 下一个造型(小猫会不断地原地踏步)
    cat.wait(0.1)            # 等待0.1秒
    im = screen.save()       # 保存当前窗口屏幕为im图形对象
    frames.append(im)        # 添加到frames列表

yes = askyesno('保存','要把每一帧动画保存到frames文件夹吗？\n否则会直接关闭窗口。')
if yes :
    for i in range(len(frames)): # 迭代刚才保存的每一帧
       im = frames[i]
       im.save(f'frames/{i}.png')
    showinfo('提示','保存完毕！')
    # 保存完毕后可以把所有的png合成一个gif
else:
    screen.bye()
    
