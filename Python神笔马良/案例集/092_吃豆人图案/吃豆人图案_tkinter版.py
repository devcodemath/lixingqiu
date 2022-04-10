"""
   吃豆人图案_tkinter版.py
"""
from tkinter import *

# 创建窗口
root = Tk()
root.title("吃豆人图案tkinter版")

# 创建画布
canvas = Canvas(root,background='#D4D4D4',width=480,height=480)
canvas.pack(fill=BOTH,expand=YES)

# 创建弧
coord = 100, 100, 400, 400    # 左上和右下坐标
arc = canvas.create_arc(coord,fill='blue',
                        start=15,extent=315,width=10)

root.mainloop()
