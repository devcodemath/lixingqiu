"""python.py,演示Python类"""

class Python:
    def __init__(self):
        self.stomach = []         # 这个属性中文为：胃

    def eat(self,food):
        """定义吃的方法"""
        self.stomach.append(food) # 给胃加食物
        
    def poop(self):
        """定义拉的方法"""
        if len(self.stomach) > 0 :
            return self.stomach.pop(0) # 弹出最先吃的
        
    def __repr__(self):
        return "蛇@" + str(id(self))

cyan_snake = Python()             # 青蛇
cyan_snake.eat("turtle")          # 青蛇吃海龟
print(cyan_snake.poop())          # 青蛇拉便便
