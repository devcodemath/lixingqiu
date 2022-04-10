"""返回lambda函数.py
本程序演示函数嵌套，定义了一个能生成直线的函数"""

def line(k,b):
    y = lambda x:k*x + b
    return y

f = line(1,2)      # 确定斜率为1，y轴截距为b的直线

print(f(2))        # 当自变量为2的时候求出y值
print(line(2,8)(2))# 打印斜率为2，截距为8,x为2时y的值
