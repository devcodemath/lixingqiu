"""
   将进酒_君不见.py
   本课主要体验序列的遍历，字符串的split命令。
"""
from sprites import *

def stepwrite(sp,string,ft):
    """逐字写字函数
    遍历字符串，每写一个字就往右移一定的距离，从而产生逐字效果。
    sp：角色,string：字符串,ft：字体样式
    """
    x = sp.xcor()                            # 记录sp的x坐标
    for char in string:                      # 对于每一个字
        sp.write(char,align='center',font=ft)# 写这个字
        sp.addx(20)                          # 往右移20个单位 
        sp.wait(0.2)                         # 等待0.2秒
    sp.setx(x)                               # 回到刚才记录的x坐标
    sp.addy(-18)                             # 往下移18个单位
        
f = open('将进酒_君不见.txt')                # 打开文件
c = f.read()                                 # 读文件
f.close()                                    # 关闭文件 

ft = ('楷体',16,'normal')                    # 定义三元组做为字体样式 
screen = Screen()                            # 新建屏幕
screen.setup(951,600)                        # 设定屏幕宽高
screen.bgpic('bg.png')                       # 贴上背景图片
screen.title('将进酒_君不见')                # 给窗口写标题

bug = Sprite()                               # 新建虫子角色
bug.goto(-10,250)                            # 定位到坐标(-10,250)

lines = c.split('\n')                        # 以换行分隔c，返回列表
for line in lines:                           # lines中的每一行  
    stepwrite(bug,line,ft)                   # 逐字写这一行

bug.wait(1)                                  # 等待1秒钟
bug.hide()                                   # 隐藏虫子
screen.mainloop()                            # 进入主循环
