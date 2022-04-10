"""自动出题器.py"""

from random import randint

result = {True:"回答正确 ",False:"回答错误 "}
 
print("简易自动出题目器")
print("-" * 20)

while True:    
    a = randint(1,100)
    b = randint(1,100)
    op = input("请选择: (+加,-减,*乘,//整除)?\n")
    if op == "" : break
    exec("c = " +  str(a) + op + str(b) ) # 把字符串当成代码执行
    answer = input(str(a) + op + str(b) + "=?\n")    
    answer = int(answer)              # 转换成整数
    print(result[answer == c],end="") # 根据字典键名打印相关提示信息

    
    
