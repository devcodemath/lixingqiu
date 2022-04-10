from sprites import *                           # 从精灵模块导入所有命令

screen = Screen()                               # 新建屏幕
screen.setup(480,480)                           # 设定屏幕大小
screen.bgcolor('dodger blue')                   # 设定背景色    
screen.bgpic('bg.png')                          # 设定背景图
screen.title('生日快乐贺卡')                    # 设定标题 

ft = ('Arial',14,'italic')                      # 定义字体样式
info = "请拖动火焰到蜡烛上,再按空格键"          # 定义开始提示语

w = Sprite(visible=False,pos=(0,150))           # 生成写字的角色
w.color('white')                                # 设为白色 
w.write(info,align='center',font=ft)            # 写提示语，请拖动火焰...

fire1 = Sprite('fires')                         # 生成火苗1
fire2 = Sprite('fires')                         # 生成火苗2

spacekey = Key('space')                         # 空格按键实例
screen.listen()                                 # 监听按键

# 下面是等待按空格键
while not spacekey.down():                      # 没按空格键时刷新屏幕
    screen.update()

fire1.play('Happy Birthday.wav',loop=True)      # 循环播放生日快乐曲子
w.clear()                                       # 清空所写的文字
w.write("Happy Birthday",align='center',font=ft)# 写字

while True:                                     # 重复执行
    fire1.nextcostume()                         # 切换到下一个造型
    fire2.nextcostume()                         # 切换到下一个造型
    screen.update()                             # 屏幕更新显示
    time.sleep(0.01)                            # 等待0.01秒
