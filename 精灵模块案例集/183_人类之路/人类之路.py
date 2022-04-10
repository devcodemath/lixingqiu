"""
   人类之路.py
   配合着扣人心弦的背景音乐，让人觉得这是一个发人生省的Python的作品。
   人类诞生以来直到今天虽然物质生活大大改善，但人类的目标是什么？
   地球没有人类是否会“过得”更好？地球是纯粹的偶然还是必然？
   生命对于宇宙的意义到底是什么？或许没有人类，“意义”这个词根本就没有意义。
   
"""
import os
from sprites import *
from PIL import Image,ImageSequence

def split_gif(gif_file):
    """拆帧函数，本函数会把gif拆帧后的文件保存为png图存放在文件夹里"""
    bgs = []
    fld = os.path.basename(gif_file).split('.')[0]    
    if not os.path.exists(fld):os.mkdir(fld)
    im = Image.open(gif_file)
    size = im.size
    index = 0
    for frame in ImageSequence.Iterator(im):
        filename = fld + os.sep + str(index) + '.png'        
        frame.save(filename)
        bgs.append(filename)
        index = index + 1
    im.close()
    return bgs,size

end_switch = False
bgs,size = split_gif('source.gif')

screen = Screen()                          # 新建屏幕对象
screen.bgcolor('black')                    # 背景颜色涂黑
screen.title('人类之路_基于Python海龟画图而创作_作者：李兴球')                   # 给窗口写上标题
screen.setup(size[0],size[1])              # 设置窗口大小

PlaySound('star.wav',SND_LOOP|SND_ASYNC)   # 循环异步播放背景音乐

# 下面的代码让背景不断地轮换显示
index = 0
def switch_background():
    global index,end_switch
    screen.bgpic(bgs[index])
    if end_switch==False:
       screen.ontimer(switch_background,100)
    index = index + 1
    index = index % len(bgs)
switch_background()

# 人类进化图
evolution = Sprite('human evolution.png')
evolution.setalpha(128)

# 下面的代码是打字幕
words = '人类从刀耕火种进化到高科技社会。让人类的生活更加美好。可是也让地球温度升高，人类生存环境遭受破坏。如果任由发展，后果不堪设想！'
e = Sprite(visible=False )              # 用来写字的对象
e.color('cyan')                         # 设定颜色为青色
e.goto(-220,200)                        # 定位到坐标(-220,200)
counter = 0                             # 计数器清零
for char in words:
    e.write(char,align='center',font=('黑体',24,'normal'))
    e.fd(37)
    counter = counter + 1
    if counter % 13 == 0 :
        e.setx(-220)
        e.addy(-40)
    e.wait(0.4)
e.wait(1)


# 下面的代码让人类进化图往下移
for _ in range(280):
    evolution.addy(-1)
    evolution.wait(0.1)

# 下面的代码以虚像效果显示未来城市图像
future = Sprite('未来城市.png',visible=False,pos=(100000,0))
future.setalpha(0)
future.home()
future.show()
for a in range(0,256):
    future.setalpha(a)
evolution.hide()            # 进化图片隐藏
end_switch = True           # 不再切换背景


# 下面的代码显示最后的话语
backtitle = Sprite('后话.png',pos=(0,300))
for _ in range(240):
    backtitle.addy(-1)
    backtitle.wait(0.1)

screen.mainloop()
