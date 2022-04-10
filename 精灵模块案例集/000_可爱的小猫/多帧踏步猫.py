from sprites import Sprite  # 从精灵模块导入Sprite类

path = 'cats'               # 相对于程序文件的cats路径

cat = Sprite(shape=path)    # 新建角色，造型为path路径下面的图像
cat.rotatemode(1)           # 设定旋转模式为左右翻转

while True:
    cat.fd(15)              # 前进15个单位        
    cat.nextcostume()       # 下一个造型
    cat.bounce_on_edge()    # 碰到边缘就反弹 
    cat.wait(0.1)           # 等待0.1秒

