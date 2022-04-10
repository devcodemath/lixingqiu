"""函数返回内部函数.py"""

def make_counter(init):
    count = init
    def counter():
        nonlocal count   # 申明非本地变量
        count += 1       # count加1
        return count
    return counter       # 返回counter函数(没加小括号)

c = make_counter(10)     # c是一个函数!
for i in range(10):
    print(c())           # 每运行一次,它的值加1
