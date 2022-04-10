"""
   三bug满屏爬单线程示例程序.py
   本程序生成三个虫子角色,分别叫bug1,bug2,bug3,
   bug定位后会不断地旋转。
   本程序需要Python精灵模块支持,请用cmd命令,打开管理员窗口,
   然后输入以下使命令进行安装:   
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites   --upgrade

"""
from sprites import Sprite,Screen

bug1 = Sprite()        # 新建虫子1

bug2 = Sprite()        # 新建虫子2 
bug2.goto(100,100)     # bug2的坐标定位到(100,100)

bug3 = Sprite()        # 新建虫子3
bug3.goto(-100,100)    # bug3的坐标定位到(-100,100)  
    
while True:            # 当成立的时候(重复执行)
    
    bug1.fd(1)         # 虫子1前进1个单位
    bug1.rt(1)         # 虫子1向右转1个单位

    bug2.fd(1)         # 虫子2前进1个单位
    bug2.rt(1)         # 虫子2向右转1个单位
    
    bug3.fd(1)         # 虫子3前进1个单位
    bug3.lt(1)         # 虫子3向左转1个单位
    
        
