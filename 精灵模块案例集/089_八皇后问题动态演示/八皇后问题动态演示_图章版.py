"""
   八皇后问题动态演示_图章版

"""
from sprites import *

width,height = 400,400
screen = Screen()
screen.title('python八皇后问题92种解决方案动态演示by李兴球')

ft = ('黑体',18,'bold')
ft2 = ('新宋体',12,'normal')
tom = Sprite(visible=False)          # 负责画格子与显示标题信息的
tom.color('magenta')
tom.addy(250)
tom.write("八皇后问题动态演示",align='center',font=ft)
tom.addy(-30)
tom.color('blue')
tom.write("本程序由Python精灵模块开发",align='center',font=ft2)
tom.home()
cors = tom.draw_grid2(8,8,50,50)     # 画8x8，长宽为50的格子图
tom.shape('res/black.png')
# 下面是画黑白相间的格子
c = 0
for rows in cors:
    index = c % 2
    for xy in rows:
        tom.goto(xy)
        if index % 2 == 0 :tom.stamp()
        index += 1
    c = c + 1
jack = Sprite('res/queen.png')

rose = Sprite(visible=False)         # 负责显示一种输出结果的
rose.sety(-250)
rose.font = ('楷体',24,'bold')
rose.color('red')

def have_conflict(x,y):
    """ 检测同列,斜线上有没有值为1的"""
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
    s = ''
    for r in grids:       # 每一行
        for c in r:       # 每行中的每个数           
            if c == 1 :
               s = s + str(r.index(c))
               print(r.index(c),end='')
    print()
    rose.clear()
    info = f'第{counter+1}种解决方案:{s}'
    rose.write(info,align='center',font=rose.font)    
        
        
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
# 键是(x,y),值是图章编号的字典
stampdict = {}                    # 保存对应坐标图章编号的字典
cleardelay = 0.005                  # 清除等待时间
setdelay = 0.005                    # 放置皇后,等待时间
resultdelay = 5                   # 找到一种结果后的等待时间
while True:
    while y < 8:                  # 每一列都不行,则回溯到上一行
        
        if have_conflict(x,y):    # 有冲突则下一列
            y = y + 1
        else:
            grids[x][y] = 1       # 否则这里放1,表示放皇后            
            jack.goto(cors[x][y])
            stampdict[(x,y)] = jack.stamp() # 保存图章编号
            jack.wait(setdelay)
            if x == 7 :           # 说明有了一个解了
                print('结果',end='')
                output()           # 输出这种结果
                
                jack.wait(resultdelay)
                counter += 1       # 计下数
                grids[x][y] = 0    # 清掉以便尝试下一列
                jack.goto(cors[x][y])
                jack.clearstamp(stampdict[(x,y)]) # 清除这个图章编号
                jack.wait(cleardelay)
                
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
            jack.goto(cors[x][i])
            jack.clearstamp(stampdict[(x,i)])
            jack.wait(cleardelay)
            y = i + 1           # 如果刚好又是8会继续回到上一行
            break
    
        
