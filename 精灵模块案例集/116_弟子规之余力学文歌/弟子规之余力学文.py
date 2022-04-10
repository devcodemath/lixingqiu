"""
   弟子规之余力学文歌.py，本程序主要演示无标题栏窗口，可拖动窗口。
   
   列表,它是以逗号隔开的,以中括号封闭的有顺序的可变数据集合。
   这些数据可以是整数、小数或者字符串。
   如[]，它是一个空列表，如[32,76,8]它是一个有三个数字的列表。
   如['中华','华夏','九州','天下']，它是一个有四个字符串的列表。
   当然，我们可以给列表取一个名字，如 x = ['Python','莽蛇']。
   本程序需要spritesv1.25版本支持，如果你无法运行，请用
   pip uninstall sprites 卸载老版本，再安装最新版本(注意缓存)
"""
from sprites import *           # 从精灵模块导入所有命令

screen = Screen()               # 新建屏幕
screen.setup(480,480)           # 设定屏幕宽高
screen.bgpic('cover.png')       # 设定背景图片
screen.titlebar(False)          # 关闭标题栏
screen.draggable()              # 按鼠标中键可拖动窗口

# 定义一个叫dzg的列表，它里面是一些字符串
dzg = ['不力行 但学文',
       '长浮华 成何人',
       '但力行 不学文',
       '任己见 昧理真',
       '读书法 有三到',
       '心眼口 信皆要',
       '方读此 勿慕彼',
       '此未终 彼勿起',
       '宽为限 紧用功',
       '工夫到 滞塞通',
       '心有疑 随札记',
       '就人问 求确义',
       '房室清 墙壁净',
       '几案洁 笔砚正',
       '墨磨偏 心不端',
       '字不敬 心先病',
       '列典籍 有定处',
       '读看毕 还原处',
       '虽有急 卷束齐',
       '有缺坏 就补之',
       '非圣书 屏勿视',
       '蔽聪明 坏心志',
       '勿自暴 勿自弃',
       '圣与贤 可驯致']
# 下面是访问列表中的每一个数据,
for s in dzg:
    print(s)

bug = Sprite(visible=False)
bug.color('black')
bug.goto(0,-200)
bug.write('按空格键播放音乐',align='center',font=('黑体',18,'normal'))


screen.listen()
spacekey = Key('space') # 实例化空格键
while not spacekey.down():screen.update()
bug.goto(-20,-10)
bug.clear()
bug.play('余力学文.wav','弟子规歌词.txt')

# 下面的TK是就是tkinter
popup = TK.Menu(screen._root, tearoff=0)
popup.add_command(label="关于本程序",command=lambda:showinfo('关于','本程序由李兴球开发\n\nQQ:406273900\n\nwww.lixingqiu.com'))
popup.add_command(label="打开主页",command=lambda:os.system('explorer http://www.lixingqiu.com'))
popup.add_command(label="退出本程序",command=lambda:screen.bye())

def do_popup(event):
    """显示弹出菜单"""
    try:
        popup.tk_popup(event.x_root, event.y_root + 10, 0)
    finally:
        # 确保释放按键
        popup.grab_release()
screen.cv.bind("<Button-3>", do_popup)   # 画布绑定鼠标右键

screen.mainloop()
