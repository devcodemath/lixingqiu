"""
   走出字母谜宫_sprites.py
   这个简单的自动走迷宫程序让I 寻找到出口就结束。
   可以加上按键检测，就变成一个小游戏。
   I表示小人，本程序需要安装sprites模块才能正常运行，安装方法：
   用cmd打开管理员窗口，输入pip install sprites
   以下是所有代码。
"""
from sprites import Sprite

def draw_maze(maze,cors):
    """画出迷宫，本函数调用一次，所以在函数内生成角色"""
    t = Sprite(visible=False)
    rows = len(maze)
    cols = len(maze[0])
    for r in range(rows):
        for c in range(cols):
            x,y = cors[r][c]
            t.goto(x,y)
            t.write(maze[r][c])
            
def draw_current(sprite,pos,maze,cors):
    """sprite在pos位置上画字母"""
    sprite.clear()           # 清除所有自己印的
    r,c = pos                # 在迷宫中的行列号
    x,y = cors[r][c]         # 把行列号换成坐标
    letter = maze[r][c]      # 需要印的字母    
    sprite.goto(x,y)
    sprite.write("I")
    sprite.wait(1)
    
maze = [['X','X','X','X','X'],
        ['X',' ',' ',' ','X'],
        ['X',' ','X',' ',' '],
        ['X',' ','X','X',' '],
        ['X',' ','X','X',' ']]

rows = len(maze)
cols = len(maze[0])
turtle = Sprite(visible=False)            # 新建隐藏角色  
cors = turtle.draw_grid2(rows,cols,50,50) # 行数，列数，格子宽，格子高
draw_maze(maze,cors)           # 画迷宫
turtle.wait(5)
bug = Sprite(visible=False)

dirs = [(-1,0),(1,0),(0,-1),(0,1)] # 方向
start = (4,1)                      # 起点
end = (4,4)                        # 终点
i = 0
while True:
    draw_current(bug,start,maze,cors) # 画当前
    if start==end:break
    for fx in dirs:            # 每一个方向
        r,c = start
        dest_row = r + fx[0]   # 目地的行位置
        dest_col = c + fx[1]   # 目地的列位置
        if maze[dest_row][dest_col]==' ': # 如果这个地方是空的则可以前进
           maze[r][c],maze[dest_row][dest_col] = maze[dest_row][dest_col],maze[r][c]
           maze[r][c] = '.'               # 雁过留声
           start = (dest_row,dest_col)
           break
   
        
