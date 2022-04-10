"""
   跳马问题算法
"""

rows = 4               # 表示行数
cols = 8               # 表示列数

grids = [ ]
for r in range(rows+1):
    grids.append([0 for i in range(cols+1)])

def outofrange(a,b):
    """是否超出范围"""
    return a > cols or b > rows or a <0 or b<0
    
x = 0
y = 0
points = [(0,0)]                         # 记录路径的
grids[0][0] = 1                          # 标记第一个点 
condition = [(1,2),(2,1),(2,-1),(1,-2)]  # 4个试探运算
records = {(0,0):-1}                     # 记录当前点已经试探过的运算 
running = True
while running:   
    # 开始试探
    if (x,y) in records:             # 如果有此键说明在此点试探过
        start = records[(x,y)]
        if start == 3 :              # 此点全部试完了,则回溯
            x,y = points.pop()
            grids[y][x] = 0          # 把此点标记为0
            records[(x,y)] = -1      # 记录此点以后需要全部测试4个方向
            if points == []:
                running = False
            else:
                x,y = points[-1]     # 从这个点重新开始
    else:
        start = -1

    for index in range(start+1,4):
        records[(x,y)] = index       # 记录此点的运算已经试探过了
        dx,dy = condition[index]
        nextx = x + dx
        nexty = y + dy        
        if outofrange(nextx,nexty):continue
        elif nextx < cols and nexty <= rows:
            grids[nexty][nextx] = 1
            points.append((nextx,nexty))
            x = nextx
            y = nexty
            break
        elif nextx == cols:
            grids[nexty][nextx] = 1
            points.append((nextx,nexty))
            if nexty == rows:  print(points)  # 到达了右上角,可输出这个路径了
            # 回溯到上一个点
            x,y = points.pop()
            grids[y][x] = 0
            records[(x,y)] = -1
            if points == []:
                running = False
            else:
                x,y = points[-1]
    
    
