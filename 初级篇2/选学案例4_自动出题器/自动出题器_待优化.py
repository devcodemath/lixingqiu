"""自动出题器_待优化.py 本程序有很多冗余的代码,可进一步优化。"""

from random import randint

print("简易自动出题目器")
print("-" * 20)

while True:

    op = input("请选择题目类型: (+加,-减,*乘,//整除 or exit)?\n")
    if op == "+":
        a = randint(1,100)
        b = randint(1,100)
        c = a + b 
        answer = input(str(a) + "+" + str(b) + "=?\n")
        answer = int(answer)
        if answer == c:
            print("回答正确")
        else:
            print("回答错误")
    elif op == "-":
        a = randint(1,100)
        b = randint(1,100)
        c = a - b 
        answer = input(str(a) + "-" + str(b) + "=?\n")
        answer = int(answer)
        if answer == c:
            print("回答正确")
        else:
            print("回答错误")
    elif op == "*":
        a = randint(1,100)
        b = randint(1,100)
        c = a * b 
        answer = input(str(a) + "*" + str(b) + "=?\n")
        answer = int(answer)
        if answer == c:
            print("回答正确")
        else:
            print("回答错误")
    elif op == "//":
        a = randint(1,100)
        b = randint(1,100)
        c = a // b 
        answer = input(str(a) + "//" + str(b) + "=?\n")
        answer = int(answer)
        if answer == c:
            print("回答正确")
        else:
            print("回答错误")
        
        
    
