"""
  角色坐标的get和set上下左右命令.py
本程序演示精灵模块角色的setleft,setright,settop,setbottom和
getleft,getright,gettop,getbottom命令。
setleft命令用来设置角色最左边的x坐标，getleft命令则是得到角色最左边的x坐标。
setright命令用来设置角色最右边的x坐标，getright命令则是得到角色最右边的x坐标。
settop命令用来设置角色最上边的y坐标，gettop命令则是得到角色最上边的y坐标。
setbottom命令用来设置角色最下边的y坐标，getbottom命令则是得到角色最下边的y坐标。

"""

from sprites import *                     # 从精灵模块导入所有命令
 
screen = Screen()                         # 新建屏幕
screen.bgcolor("#003278")                 # 背景颜色
redsquare = Image.new(size=(100,100),
                    mode="RGBA",
                    color=(255,0,0,255))   # 新建100x100的红色图形
redsquare.save('redsquare.png')            # 保存为图像

redsquare = Sprite("redsquare.png")        # 新建角色
redsquare.color('white')                   # 画笔颜色为白色 
redsquare.draw_grid2(4,4,100,100)          # 画4x4,宽高100x100的格子
redsquare.setleft(0)                       # 设置角色最左x坐标为0   
redsquare.settop(100)                      # 设置角色最顶y坐标为100 
left = redsquare.getleft()                 # 获取角色最左x坐标 
top = redsquare.gettop()                   # 获取角色最顶y坐标
right = redsquare.getright()               # 获取角色最右x坐标
bottom = redsquare.getbottom()             # 获取角色最下y坐标
print(left,top,right,bottom)
while True:                                # 当成立的时候
  redsquare.setright(100)                  # 设置角色最右x坐标为100 
  redsquare.wait(0.5)                      # 等待0.5秒 
  redsquare.setbottom(-100)                # 设置角色最底y坐标为-100 
  redsquare.wait(0.5)
  redsquare.setleft(-100)                  # 设置角色最左x坐标为-100 
  redsquare.wait(0.5)
  redsquare.settop(100)                    # 设置角色最顶y坐标为100 
  redsquare.wait(0.5)

  
