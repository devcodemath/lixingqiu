"""
   青青河边草.py
   本程序会演示一个动画,并且每隔100帧对动画进行截屏,
   截成的图像并没有立即写入到硬盘中,而是临时放在列表,
   当动画完成后,最后一次性写入硬盘里。
"""
import time                                     # 导入时间模块
from sprites import *                           # 从精灵模块导入所有命令

screen = Screen()                               # 新建屏幕
screen.setup(600,399)                           # 设定屏幕宽高
screen.bgpic('河边草.jpg')                      # 铺上背景图
screen.titlebar(False)                          # 去掉标题栏
screen.addpopup()                               # 绑定右键菜单
screen.draggable()                              # 按中键可拖动

# 定义角色的造型列表
images = ['金铭.jpg','金铭2.jpg','金铭3.jpg',
          '三人照.jpg','海报.jpg','海报2.jpg',
          '金铭4.jpg','两人.jpg','风雨.jpg']

frames = []                                    # 帧图列表,保存截取屏幕的图形对象
pic = Sprite(shape='海报2.jpg')                # 新建角色
pic.play('青青河边草.wav')                     # 放音乐,它有186秒时长
begin = time.time()                            # 记录开始播放时间
index = 0                                      # 索引号从0开始
counter = 0                                    # 这个做为帧计数器
while True:                                    # 当成立的时候
    # 以下段落让角色在屏幕中央盖一个图章,如果x坐标大于400则换一个造型从左边出来    
    if pic.xcor()==0:                          # 如果pic的x坐标和0相等
        pic.clearstamps()                      # 清除以前的图章
        pic.stamp()                            # 盖图章
    pic.fd(1)                                  # 前进1个单位
    left,top,right,bottom = pic.bbox()         # 获取绑定盒子(左上角和右下角坐标)
    if left > 400:                             # 如果最左x坐标大于400 
        index = index + 1                      # 索引增加1
        index = index % 9                      # 索引号对9求余
        pic.shape(images[index])               # 设定造型图
        left,top,right,bottom = pic.bbox()     # 重新获取绑定盒
        w = (right-left)/2                     # 计算图片宽度的一半
        pic.setx(-300-w)                       # 设定角色的x坐标
        
    if counter % 100 == 0 :                    # 计数器对100求余则截屏           
       im = screen.save()                      # 保存当前这一帧图到内存
       frames.append(im)                       # 添加im图形对象到帧列表
    counter = counter + 1                      # 帧计数器增加1
    time.sleep(0.01)                           # 等待0.01秒
    时间 = time.time() - begin                 # 计算逝去的时间
    if 时间 > 186:break                        # 如果时间大于186秒,则中断循环
    
print('本程序共产生',len(frames),'帧图,下面保存frames中所有的图形对象到文件夹中')

for i in range(len(frames)):
    im = frames[i]
    filename = 'ims/' + str(i) + ".png"
    im.save(filename)
    
        
