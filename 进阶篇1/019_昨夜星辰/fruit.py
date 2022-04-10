"""fruit.py 本程序提供 水果类的定义"""

class Fruit:
    """水果类"""
    def __init__(self,w,c):
        self.weight = w         #重量属性，初始化值为w
        self.color = c          #颜色属性，初始化值为c
        
    def addweight(self,w):
        """让水果增加重量w"""
        self.weight = self.weight + w
        
    def getweight(self):
        """返回重量"""
        return self.weight
 
if __name__ == "__main__":
    
    a = Fruit(50,"red")
    a.addweight(50)        #让a增加重量50
    a.getweight()          #调用getweight方法获取a的重量 
    a.brand = "编程娃娃"   #给a增加属性名为brand
    print(a.brand)

