
from sprites import Sprite # 从精灵模块导入Sprite命令

for x in range(16):
    s = Sprite(x)           # 0代表虫子,1代表弹球
    s.setx(x*30-300)
    s.say(str(x),delay=1000,wait=False)
