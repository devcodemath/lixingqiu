"""
   走出字母谜宫.py
   这个简单的程序让I字母寻找到出口就结束。
   可以加上按键检测，就变成一个小游戏。
   I是起点
"""
def output_maze(maze):
    for row in maze:
        print(row)
    print()

maze = [['X','X','X','X','X'],
        ['X',' ',' ',' ','X'],
        ['X',' ','X',' ',' '],
        ['X',' ','X','X',' '],
        ['X','I','X','X',' ']]

dirs = [(-1,0),(1,0),(0,-1),(0,1)] # 方向

start = (4,1)                # 起点
end = (4,4)                  # 终点
i = 0
while True:
    output_maze(maze)
    if start==end:break
    for fx in dirs:          # 每一个方向
        r,c = start
        dest_row = r + fx[0]
        dest_col = c + fx[1]
        if maze[dest_row][dest_col]==' ': # 如果这个地方是空的则可以前进
           maze[r][c],maze[dest_row][dest_col] = maze[dest_row][dest_col],maze[r][c]
           maze[r][c] = '.'               # 雁过留声
           start = (dest_row,dest_col)
           break
   
        
