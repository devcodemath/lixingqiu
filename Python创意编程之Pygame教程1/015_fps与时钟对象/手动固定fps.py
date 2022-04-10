"""
   手动固定fps动画。
   本程序会让while循环固定在限定的时间内运行一次。
"""

import pygame
import time

width,height = 543,360
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("中秋快乐动画")

# 加载所有的图形帧,转换成surface
images = [pygame.image.load(f"中秋快乐/{index:04d}.png")
          for index in range(1,30)]

amounts = len(images)
index = 0
running = True

fps = 10
while running:
    start_time = time.time()          # 记录起始时间
    for event in pygame.event.get():  # 遍历每个事件 
        if event.type == pygame.QUIT:running = False
    image = images[index]             # 取一张图片
    index = index + 1                 # 索引号加1
    index = index % amounts           # 对数量求余
    screen.fill((0,0,0))              # 填充背景颜色  
    screen.blit(image,(0,0))          # 贴到screen上
    pygame.display.update()           # 更新屏幕显示 
    pygame.display.set_caption("fps=" + str(fps))
    t = time.time() - start_time      # 计算上面代码运行的时间
    if t < 1/fps : wait_time = 1/fps - t
    time.sleep(wait_time)
pygame.quit()
        
