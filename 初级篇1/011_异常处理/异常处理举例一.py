"""异常处理举例一.py"""
 
try:
    f = open("武林秘籍.txt")
    功夫 = f.read()
    f.close()
except:
    功夫 = '九阴真经,葵花宝典,凌波微步,Python编程'

print(功夫)
    
