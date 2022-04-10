"""
   角色对话
"""
from sprites import Sprite

cat1 = Sprite(2)                # 新建角色,2代表小猫
cat1.say('你好')                # 角色说话,不加参数也会说你好

cat2 = Sprite(2)                # 新建角色,2代表小猫
cat2.fd(100)                    # 角色前进100
cat2.rotatemode(2)              # 角色旋转模式为左右翻转
cat2.setheading(180)

# 延时为10秒,阻塞,即要10秒后才会运行下一行代码
cat2.say('你也好',delay=10,wait=True) 
cat2.say('单击屏幕任何地方关闭窗口')
cat1.screen.exitonclick()
