"""
    星汉灿烂的序幕模块.py
    本程序使用Pygame来播放一个gif动图。
"""
import os
import pygame
from pygame.locals import *
from tempfile import TemporaryDirectory
from PIL import Image, ImageSequence
 
def playgif(imagefile,screen_width=480,screen_height=360,bgmusic=None):
    """加载gif文件,渲染在Pygame的屏幕上不断显示"""
    
    pygame.init()
    center = screen_width//2,screen_height//2
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("星汉灿烂_作者:李兴球")

    # 下面显示请稍候的提示
    default_font = pygame.font.get_default_font()
    myfont = pygame.font.Font(default_font,22)
    myfont = myfont.render('Please wait...',True,(0,128,128))
    w,h = myfont.get_size()
    center = center[0]-w//2,center[1]-h//2
    screen.blit(myfont,center)
    pygame.display.update()
    
    basename = os.path.basename(imagefile)
    basename = basename.split('.')[0]
    outputframes = []              # 待返回的每一帧
    # 新建临时文件夹
    ffd = TemporaryDirectory(suffix=None, prefix=None, dir=None)     
    im = Image.open(imagefile)   # 载入图片
    width,height = im.size
    index = 0
    # 下面是拆帧过程,下一个版本将把pillow图像转换成bytes,
    # 然后在Pygame中通过pygame.image.fromstring直接转为surface
    print("读取gif文件中,请稍候...")
    for frame in ImageSequence.Iterator(im): # 迭代gif图中的每一帧
        filename = ffd.name + os.sep +  basename +  str(index) + ".png"
        frame.save(filename )
        outputframes.append(filename)
        index += 1
    im.close()                  # 关闭图形对象

    try:                        # 尝试播放背景音乐
        pygame.mixer.init()
        pygame.mixer.music.load(bgmusic)
        pygame.mixer.music.play(-1,0)
    except:
        pass

    # 下面是新建屏幕显示每一帧图,从而就能播放gif动画，
    # 由于临时文件会被自动删除，所以不单独设一个函数。
    # 播放完毕后，拆帧所产生的png会被自动清理掉。
    frames = [pygame.image.load(im) for im in outputframes]   
    index = 0
    amounts = len(frames)
    rect = pygame.Rect(0,0,width,height)
    rect.center = screen_width//2,screen_height//2
    clock = pygame.time.Clock()
    for index in range(amounts):
        screen.fill((0,0,0))
        screen.blit(frames[index],rect)
        pygame.display.update()
        clock.tick(10)
    
    return screen

if __name__ == "__main__":
        
    width,height = 480,360    
    screen = playgif('序幕.gif',width,height)
    if screen:pygame.quit();print(screen)

