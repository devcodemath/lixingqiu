"""
   相思配图(图章虚像效果).py
"""

from sprites import *                     # 从精灵模块导入所有命令

width,height = 531,800
screen = Screen()                         # 新建屏幕
screen.setup(width,height)                # 设宽度高
screen.bgpic('姑娘和背景x.png')           # 设定背景
screen.title('相思配图(图章虚像效果)by李兴球')

# 新建girl角色
girl = Sprite(shape='girl.png',pos=(-22,-26))
girl.setalpha(128)                          # 设为半透明
s1 = girl.stamp()                           # 盖虚像图章
s2 = girl.stamp()                           # 盖虚像图章

song = Sprite(visible=False)                # 播放歌曲的隐藏角色
song.color('cyan','blue')
# 下面的播放会根据lrc在屏幕上显示歌词
song.play('相思（西游记后传片毛阿敏-）.wav','相思歌词.lrc')

clock = Clock()                          # 实例化时钟对象
for x in range(500):                     # 迭代x伍百次
   girl.movestamp(s1,-1,1)               # s1图章向左上角移动
   girl.movestamp(s2,1,1)                # s2图章向右上角移动
   screen.update()                       # 屏幕显示更新
   clock.tick(30)                        # 固定fps为30
  
dummy = Sprite(visible=False,pos=(52,316))
dummy.saybordercolor('cyan')              # 说话泡泡边框的颜色
dummy.saycolor('yellow')                  # 说话泡泡里面字的颜色
dummy.say("Hi，雅典娜，你好吗？",100,wait=False)

screen.mainloop()
