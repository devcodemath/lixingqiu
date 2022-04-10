"""
   拼图游戏教学版.py
"""
import os
from random import randint
from PIL import Image
from sprites import Sprite,Screen

def shuffle(array):
    rows = len(array)
    cols = len(array[0])
    for _ in range(5):
        i = randint(0,rows-1)
        j = randint(0,cols-1)
        r = randint(0,rows-1)
        c = randint(0,cols-1)
        if (i,j)!=(r,c):
            tmp = array[i][j]
            array[i][j] = array[r][c]
            array[r][c] = tmp
            
class TuKuai:
    def __init__(self,data,raw_pos):
        """图块类,记录图形对象和原始所在的行列号"""
        self.data = data        # data是一个角色Sprite
        self.raw_pos = raw_pos  # 应该所在的位置
        self.current_pos = raw_pos # 当前位置
        
class Game:
    def __init__(self,pic,m):
        """pic:pillow图像对象,m需要分割的行列号"""
        fd = os.path.dirname(pic)
        name = os.path.basename(pic).split('.')[0]
        if not os.path.exists(fd + os.sep + name):
            os.mkdir(fd + os.sep + name)
        self.pic_name = name
        self.pic = Image.open(pic)
        self.pic_width = self.pic.width
        self.pic_height = self.pic.height
        self.pic_left_center = -self.pic.width//2 # 左上角格子中心点x坐标
        self.pic_top_center = self.pic.height//2  # 左上角格子中心点y坐标
        
        self.m = m
        self.block = []            # 存储分割的每个图块
        self.split_image()         # 按mxm分割图形 
        #shuffle(self.block)        # 打乱顺序  
        
    def split_image(self):
        im = self.pic
        w,h = im.size        
        # 下面分割图像
        x ,y = 0,0
        for i in range(self.m):
            row = []
            for j in range(self.m):            
                box = (x,y,x+w//self.m,y+h//self.m)
                x = x + w//self.m
                pic = im.crop(box)
                fn = f'res/{self.pic_name}/{self.pic_name}_{i}_{j}.png'
                pic.save(fn)
                raw_pos_x = self.pic_left_center + j * self.pic_width//self.m
                raw_pos_y = self.pic_top_center - i * self.pic_height//self.m
                square = Sprite(fn,pos=(raw_pos_x,raw_pos_y))
                tk = TuKuai(square,(i,j))
                row.append(tk)
            self.block.append(row)
            x = 0
            y = y + h/self.m

if __name__ == '__main__':

    screen = Screen()
    Game('res/thunder.png',3)
    screen.mainloop()
