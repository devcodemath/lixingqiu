"""
   迷宫房间类游戏,这里提供一个雏形,方便学习。
"""

from sprites import *

maze1 = ["1111111111",
         "1000000001",
         "1001110101",
         "1000010101",
         "1000010001",
         "1001001001",
         "1000100001",
         "1000000001",
         "1011100111",
         "1111111111"]

tile_width = tile_height = 80     # 砖块宽度和高度
rows = len(maze1)                 # 行的数量
cols = len(maze1[0])              # 列的数量
maze_height = rows * tile_height  # 迷宫的高度
maze_width = cols * tile_width    # 迷宫的宽度

screen = Screen()                 # 新建屏幕
screen.setup(maze_width,maze_height)
screen.title('迷宫房间类游戏,请按上下左右方向箭头')

# 左上角起始铺砖点
startx = -maze_width//2 + tile_width//2 
starty = maze_height//2 - tile_height//2

cors = {}                       # 记录每个铺砖点是否有砖
t = Sprite(shape='tile.png')

for i in range(rows):
    for j in range(cols):          
         flag = maze1[i][j]     
         x = startx + j * tile_width
         y = starty - i * tile_height
         # 记录中心点处是否有砖  
         cors[(x,y)] = flag
         if int(flag):
             t.goto(x,y) 
             t.stamp()

# 下面是新建一个人,它只能在没有砖的地方移动
r = Sprite(shape='ren.png',visible=False)

# 下面是找个没有砖块的地方出现 
while not r.isvisible():
    x,y = random.choice(list(cors.keys())) # 随机寻找一个空的地方
    if cors[(x,y)] == '1':continue         # 如果此处有砖,则继续寻找
    r.goto(x,y)                            # 否则让小人到达这个地方
    r.show()                               # 并且显示出来 

def move_left():
    """基于预判的'碰撞检测'"""
    x = r.xcor() - tile_width
    y = r.ycor()
    if cors[(x,y)] == "0" : r.setx(x)
    
def move_right():
    x = r.xcor() + tile_width
    y = r.ycor()
    if cors[(x,y)] == "0" : r.setx(x)
    
def move_up():
    x = r.xcor() 
    y = r.ycor() +  tile_height
    if cors[(x,y)] == "0" : r.sety(y)
    
def move_down():
    x = r.xcor() 
    y = r.ycor() -  tile_height
    if cors[(x,y)] == "0" : r.sety(y)

screen.onkeypress(move_left,'Left')
screen.onkeypress(move_right,'Right')
screen.onkeypress(move_up,'Up')
screen.onkeypress(move_down,'Down')

screen.listen()
screen.mainloop()
        




