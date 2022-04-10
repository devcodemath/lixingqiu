from sprites import *

def cangoto(i,j):
    """返回是否能到达i,j位置"""
    if i<rows and j<cols:
        if maze[i][j]==0:
            return True
    return False

maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
      [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
      [1,0,1,0,1,1,1,1,0,1,0,1,0,1],
      [1,0,1,0,0,0,0,0,0,1,1,1,0,1],
      [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
      [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
      [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
      [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
      [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
      [1,0,1,0,0,0,1,0,0,1,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

cols = 14                           # 列数
rows = 12                           # 行数  

screen = Screen()
screen.tracer(0,0)
screen.setup(800,600)

bug = Sprite(shape='square')        # 新建方形对象
bug.shapesize(2.5)
cors = bug.draw_grid2(rows,cols)    # 画rows行,cols列,宽高各50的格子
bug.clear()                         # 清除所有格子
# 格子标为1的印上黑色正方形
for r in range(rows):
    for c in range(cols):
        if maze[r][c]==1:           # 如果这个位置是1 
            bug.goto(cors[r][c])    # bug到达这个位置的坐标
            bug.stamp()             # 印黑正方形
bug.shape('res/bug.png')            # bug 修改造型 
bug.scale(1)                        # 修正比例
bug.goto(cors[1][1])                # 到达起始点
bug.dest= False                     # 自定义属性
screen.update()
counter = 0
def walk_maze(r,c,endr,endc):       # 递归函数(深度搜索)  
    """r,c:起点,endr,endc:终点"""
    global counter
    # 寻找所有可用的方向
    for i,j in dirs:
        if cangoto(r+i,c+j):        # 如果前面这一格是空
            r += i
            c += j
            if bug.dest == False:   # 如果没到达目的地
               bug.goto(cors[r][c]);bug.wait(0.2)
               screen.save(f"frames/{counter}.png")
               counter += 1
            maze[r][c] = 1
            stack.append((r,c))                
            if r==endr and c==endc: # 如果到达目的地了
                bug.dest = True                     
            else:walk_maze(r,c,endr,endc)
    else:       
       if stack:
           r,c = stack.pop()
           if bug.dest == False:   # 如果没到达目的地
               bug.goto(cors[r][c]);bug.wait(0.2)
               screen.save(f"frames/{counter}.png")
               counter += 1
           walk_maze(r,c,endr,endc)

r,c = 1,1                          # 起点
endr,endc = 10,12                  # 终点
txt2image('起','res/起点.png')     # 文字转图
txt2image('终','res/终点.png')     # 文字转图
dummy = Sprite(visible=False)
dummy.shape('res/起点.png')
dummy.goto(cors[r][c])
dummy.stamp()
dummy.shape('res/终点.png')
dummy.goto(cors[endr][endc])
dummy.stamp()

stack = []
dirs = [(1,0),(0,1),(-1,0),(0,-1)]  # 4个方向
stack.append((r,c))                 # 起点添加到stack中
walk_maze(r,c,endr,endc)

screen.mainloop()
            

