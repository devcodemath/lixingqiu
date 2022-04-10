"""算法就是为了解决某一个问题而采取的具体有效的操作步骤


本程序不用max命令,把最大的数据打印出来,请修改程序,打印最大数据的索引号"""

from random import randint

data = [randint(-100,100) for i in range(10)]

max_data = data[0]          # 假设索引为0的数据最大

for i in range(1,10):       # 遍历其它数据
    if data[i] > max_data:  # 发现更大的数据
        max_data = data[i]  # 所以 max_data就应该换成这个更大的

print(data)
print(max_data)
        
