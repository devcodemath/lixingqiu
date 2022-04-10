"""
   吃豆小虫.py
   本程序有一个外置模块叫mazemake。这个模块中有一个叫make_image的函数。
   它能生成图像，可以有边框，图像的颜色和边框厚度与颜色都是可以设置的。
   
   它还有一个make_maze能把一个文本文件转换成一个迷宫。
   迷宫的砖块都是用一张图片做为角色，让角色所盖的图章。
   需要相关的知识为图章列表，它的名字叫stampItems。
   这个stampItems存储了角色所盖的所有图章的编号。
   make_maze函数返回屏幕对象以及角色对象和没有盖图章的所有坐标点。
   
   本程序还要理解find_overlapping中排除参数的用法。
   角色的find_overlapping是查找所有和它有矩形重叠的项目编号。
   如果想让角色不对某些项目进行碰撞检测，那么可以加一个参数，这叫排除参数。
   排除参数可以是列表或元组，也可以是一个整数，或者一个字符串。
   如果是列表或元组，则遍历它。把每个号码都进行排除。
   如果是整数，直接把这个号码排除。
   如果是字符串，则认为是某类角色的标签，会把这一类角色的编号都进行排除。
"""
from sprites import *                   # 从精灵模块导入所有命令
from mazemake import *                  # 从迷宫生成模块导入所有命令

pic = make_image(50,50)                 # 生成50x50的图像  
pic.save('c:/a.png')                    # 保存图像
screen,square,nullcors = make_maze('maze.txt','c:/a.png')

bean = Sprite(shape='circle',visible=False) # 新建豆子角色，用盖图章的方法产生豆子
bean.color('green')
bean.scale(0.3)
for x,y in nullcors:
    bean.goto(x,y)
    bean.stamp()                        # 绿色的豆子是一个图章
dots = bean.stampItems                  # 给图章列表取一个别名

bug = Sprite(pos=(-25,0))               # 生成虫子角色
bug.scale(0.8)                          # 把虫子变小一点

speed = 6                               # 虫子移动的单位距离
leftkey = Key('Left')                   # 新建左方向箭头
rightkey = Key('Right')                 # 新建右方向箭头
upkey = Key('Up')                       # 新建上方向箭头
downkey = Key('Down')                   # 新建下方向箭头
screen.listen()                         # 监听屏幕按键 

while dots:                             # 当dots列表还有图章时候(有豆子)
    if leftkey.down():
        bug.setheading(180)             # 面向左的方向 
        bug.addx(-speed)                # 按左键则往左移
        # 查找所有和bug有碰撞的项目，豆子除外。
        if bug.find_overlapping(dots):bug.addx(speed)
    if rightkey.down():
        bug.setheading(0)               # 面向右的方向
        bug.addx(speed)                 # 按右键则往右移
        if bug.find_overlapping(dots):bug.addx(-speed)
    if upkey.down():
        bug.setheading(90)              # 面向上的方向
        bug.addy(speed)                 # 按上键则往上移
        if bug.find_overlapping(dots):bug.addy(-speed)
    if downkey.down():
        bug.setheading(-90)             # 面向下的方向
        bug.addy(-speed)                # 按下键则往下移
        if bug.find_overlapping(dots):bug.addy(speed)
    items = bug.find_overlapping(square.stampItems)  # 除墙壁外的所有的豆子的碰撞检测
    [bean.clearstamp(item) for item in items]        # 清除碰到的豆子
         
    screen.title(str(len(dots)))
    screen.update()
    time.sleep(0.01)
    
screen.title('虫子已经吃完所有豆豆了')
bug.home()
bug.write('Game Over',align='center',font=('',32,'normal'))
screen.mainloop()
