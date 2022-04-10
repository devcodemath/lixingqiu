"""
    动态图片播放模块.py
    本程序使用Pygame来播放一个gif动图。
    gif图是通过pillow模块的Image类打开的,
    通过把它转换成bytes,从而让Pygame.image.fromstring
    能读取这个图形到内存，进而一帧一帧地显示在screen上。
"""
import pygame
from PIL import Image,ImageSequence
 
def playgif(imagefile,sw=480,sh=360,bgmusic=None):
    """imagefile:图形文件,sw:屏幕宽度,sh:屏幕高度,bgmusic:背景音乐
       ,本函数加载gif文件,渲染在Pygame的屏幕上不断显示从而播放gif图形。"""
    
    pygame.init()
    screen = pygame.display.set_mode((sw,sh))
    pygame.display.set_caption(imagefile)
    
    gif_image = Image.open(imagefile) # 打开gif文件
    width,height = gif_image.size   
   
    print("读取gif文件中,请稍候...")
    frames = []                       #  帧列表

    # 拆帧过程，迭代gif图中的每一帧
    for frame in ImageSequence.Iterator(gif_image): 
        frame = frame.convert(mode="RGB")
        im = frame.tobytes()          # 转换为字节类型数据
        frame = pygame.image.fromstring(im,(width,height),"RGB")
        frames.append(frame)        
    gif_image.close()                  # 关闭图形对象

    try:                               # 尝试播放背景音乐
        pygame.mixer.init()
        pygame.mixer.music.load(bgmusic)
        pygame.mixer.music.play(-1,0)
    except:
        pass

    # 下面是用Pygame窗口显示每幅帧图
    rect = pygame.Rect(0,0,width,height)
    rect.center = sw//2,sh//2
    clock = pygame.time.Clock()
    for frame in frames:
        pygame.event.get()
        screen.fill((0,0,0))
        screen.blit(frame,rect)
        pygame.display.update()
        clock.tick(10)
    
    return screen

if __name__ == "__main__":        
      
    screen = playgif('序幕.gif')
    print(screen)

