"""异常处理举例二.py"""
 
try:
    f = open("武林秘籍.txt")
    功夫 = f.read()
    f.close()
except FileNotFoundError:
    print("没有找到'武林秘籍.txt'文件,将会使用默认的功夫.")
    功夫 = '九阴真经,葵花宝典,凌波微步,Python编程'
except:
    print("发生意外错误,将会使用默认的功夫.")
    功夫 = '九阴真经,葵花宝典,凌波微步,Python编程'
    
print(功夫)
    
