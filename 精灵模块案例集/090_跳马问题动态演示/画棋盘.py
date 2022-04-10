"""
   为跳马问题而制作的棋盘程序
"""
from sprites import * 

grid_width  = 50       # 格子宽度
grid_height = 40       # 格子高度
rows = 4               # 表示行数
cols = 9               # 表示列数
chess_width = grid_width * cols
chess_height = grid_height * rows

screen = Screen()      # 新建屏幕
s = Sprite()
s.draw_grid2(rows,cols,grid_width,grid_height)

left,bottom = -chess_width/2,-chess_height/2
print(left,bottom)     # 左下角坐标

cors = []              # 每个顶点的坐标
for r in range(rows+1):
    rcors = []
    for c in range(cols+1):
        x = left + c * grid_width
        y = bottom + r * grid_height
        rcors.append((x,y))
    cors.append(rcors)
        
