"""apple.py 本程序定义苹果类,它继承自Fruit类"""

from fruit import *                  #导入Fruit类
 
class Apple(Fruit):                  #继承自Fruit
    def __init__(self,w,c):
        Fruit.__init__(self,w,c)     #父类初始化
        self.shape = '圆形'
        
    def getshape(self):
        print("我的形状是：" + self.shape)
        
if __name__ == "__main__":
    
    a = Apple(50,"red")
    a.addweight(50)
    print(a.getweight())
    a.getshape()
 
