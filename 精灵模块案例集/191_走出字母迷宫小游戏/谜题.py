# 习题3-5 谜题 (Puzzle,ACM/ICPC World Finals 1993,UVa227)

def output_chess(chess):
    for row in chess:
        print(row)
    print()

chess = [['T','R','G','S','J'],
         ['X','D','O','K','I'],
         ['M',' ','V','L','N'],
         ['W','P','A','B','E'],
         ['U','Q','H','C','F']]

fx = {'A':(-1,0),'B':(1,0),'L':(0,-1),'R':(0,1)} # 方向
cmds = input("请输入指令以0结束:")
r,c = (2,1)                # 当前的空格位置
i = 0
while True:
    output_chess(chess)
    code = cmds[i]
    if code =='0':break
    if code not in fx:
        print("非法指令")
        break
    dest_row = r + fx[code][0]
    dest_col = c + fx[code][1]
    chess[r][c],chess[dest_row][dest_col] = chess[dest_row][dest_col],chess[r][c]
    r = dest_row
    c = dest_col
    i = i + 1
