
from sprites import Sprite # 从精灵模块导入Sprite命令

ball = Sprite(1)           # 0代表虫子,1代表弹球

while True:
    ball.fd(0.1)           # 前进0.1
    ball.bounce_on_edge()  # 碰到边缘就反弹
