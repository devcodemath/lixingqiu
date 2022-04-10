"""查找关键词简单示例.py"""

s = '风火轮编程培训中心可以学习Python编程和Scratch编程及C编程吗?'

index = 0
keywords = '编程'
length = len(keywords)

while True:
    index = s.find(keywords,index)  # 从索引index开始查找关键词
    if index == -1:break            # 没找到则中断循环
    print(index)                    # 打印所找到的索引号
    index = index + length          # 为了继续查找,所以加上length
    
