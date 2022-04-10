"""
   本程序运行后会有一只小猫向前走,
   需要sprites模块支持,pip install sprites
"""

from sprites import Sprite             # 从精灵模块导入Sprite类

images = 'res/cat1.png','res/cat2.png' # 两张猫的造型图

cat = Sprite(shape=images)             # 新建角色,造型序列为images
cat.play('喵.wav')                     # 播放喵声

while True:                            # 当成立的时候(重复执行)
    cat.fd(10)                         # 前进10
    cat.nextcostume()                  # 下一个造型
    cat.wait(0.3)                      # 等待0.3秒
