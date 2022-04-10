"""
   八皇后问题算法by李兴球

"""
def have_conflict(x,y):
    """ 检测同列,斜线上有没有值为1的
        x:行号
        y:列号
    """
    for r in range(x):   # 同列,不超过第x行,因为下面的没必要检测         
        if grids[r][y] == 1 :return True
    # 左上斜检测
    r = x
    c = y
    while True:
        r = r-1
        c = c-1
        if r < 0 or c < 0 :break
        if grids[r][c] == 1 : return True

    # 右上斜检测
    r = x
    c = y
    while True:
        r = r-1
        c = c+1
        if r < 0  or c > 7  :break
        if grids[r][c] == 1 : return True
    
def output():
    for r in grids:       # 每一行
        for c in r:       # 每行中的每个数
            if c == 1 :print(r.index(c),end='')
    print()
        
        
grids = [[0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)],
         [0 for i in range(8)]]
x = 0                             # x表示行
y = 0                             # y表示列
counter = 0
while True:
    while y < 8:                  # 每一列都不行,则回溯到上一行
        
        if have_conflict(x,y):    # 有冲突则下一列
            y = y + 1
        else:
            grids[x][y] = 1       # 否则这里放1,表示放皇后
            if x == 7 :           # 说明有了一个解了
                print('结果',end='')
                output()           # 输出这种结果
                counter += 1       # 计下数
                grids[x][y] = 0    # 清掉以便尝试下一列
                y = y + 1          # 尝试下一列,向右移尝试
            else:
                x = x + 1          # 下一行
                y = 0              #  从0列开始
            
    # 如果所有的y位置都不行,回到上一行
    x = x - 1
    if x == -1 :break
    # 寻找上一行的y
    for i in range(8):
        if grids[x][i] == 1:
            grids[x][i] = 0     # 清除这种
            y = i + 1           # 如果刚好又是8会继续回到上一行
            break
    
        
