"""
  自动寻路.py
  本程序使用角色的coloroverlap命令检测自己身上的颜色和其它角色上面的颜色是否重叠。
  需要Python精灵模块V1.35版本以上支持。如果你的电脑没有安装Python精灵模块，
  请在命令提示符下输入以下命令进行安装：
  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites --upgrade
"""
from sprites import Sprite,Screen

screen = Screen()                     # 新建屏幕
screen.setup(960,720)                 # 设定宽高 
screen.colormode(255)                 # 颜色模式
screen.title("自动寻路_Python精灵模块_颜色碰撞示例_李兴球博客_www.lixingqiu.com")

red = (255,0,0)                       # 红色
blue = (0,63,255)                     # 蓝色
brown = (102,102,0)                   # 棕色                    
green = (0,255,0)                     # 绿色

maze = Sprite('path.png')             # 路径角色
maze.ondrag(None)                     # 不可拖动

cat = Sprite('cat.png',pos=(-50,280)) # 猫角色
cat.wait(3)
cat.left(180)                         # 向后转180度
cat.wait(1)
while True:
    cat.fd(6)                         # 猫前进6个单位
    p = cat.coloroverlap(blue,brown)  # 蓝色和棕色重叠检测
    if p: cat.left(10)                # 如果重叠了则向左转
    p = cat.coloroverlap(red,brown)   # 红色和棕色重叠检测
    if p: cat.right(10)               # 如果重叠了则向右转
    b = cat.collidecolor(green)       # 角色和绿色碰撞检测 
    if b:break                        # 如果碰到了则中断循环
    screen.update()                   # 刷新屏幕显示
screen.mainloop()
