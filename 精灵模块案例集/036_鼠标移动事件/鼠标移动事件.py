"""
   鼠标移动事件.py
"""

from sprites import  *              #  从精灵模块导入所有命令

def follow(x,y):
    """跟随鼠标指针"""
    global a
    bug.clear()                     # 清空所有轨迹
    bug.goto(x,y)                   # 定位到x,y坐标
    bug.write("中国风火轮编程",align='center',angle=a)
    a = a  + 1

a = 0
screen = Screen()                   # 新建屏幕
screen.bgcolor('dodger blue')       # 设置背景色

bug = Sprite(visible=False)         # 新建隐藏的精灵对象
bug.color('white')                  # 设定颜色为白色

screen.onmousemove(follow)          # 绑定follow函数
screen.mainloop()                   # 进入主循环
