"""
   迷宫房间类游戏,这里提供一个雏形,方便学习。
"""

from sprites import *

def keyscheck():
    if akey.down():
        while akey.down():screen.update() # 等待松开a键   
        x = r.xcor() - tile_width
        y = r.ycor()
        if cors[(x,y)] == "0" : r.setx(x)
    
    elif dkey.down():
        while dkey.down():screen.update() # 等待松开d键
        x = r.xcor() + tile_width
        y = r.ycor()
        if cors[(x,y)] == "0" : r.setx(x)
        
    elif wkey.down():
        while wkey.down():screen.update()
        x = r.xcor() 
        y = r.ycor() +  tile_height
        if cors[(x,y)] == "0" : r.sety(y)        
        
    elif skey.down():
        while skey.down():screen.update()
        x = r.xcor() 
        y = r.ycor() -  tile_height
        if cors[(x,y)] == "0" : r.sety(y)
        
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
maze_height  = cols * tile_height # 总共的宽度
maze_width = rows * tile_width    # 总共的高度

screen = Screen()                 # 新建屏幕
screen.setup(maze_width,maze_height)
screen.title('迷宫房间类游戏,请按awsd键')

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
while True:
    x,y = random.choice(list(cors.keys()))
    if cors[(x,y)] == '0':
        r.goto(x,y)
        r.show()
        break   

akey = Key('a')
dkey = Key('d')
wkey = Key('w')
skey = Key('s')
screen.listen()

while 1:
    keyscheck()
    screen.update() 
        
    

        




