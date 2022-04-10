"""if语句四种形式.py"""

from random import randint
a = randint(1,100)
b = randint(1,100)

#形式一:
if a>b:
    print("a>b")

#形式二:
if a>b:
    print("a>b")
else:
    print("a不大于b")

#形式三:
if a>b:
    print("a>b")
elif a==b:
    print("a和b的值相等")
elif a<b:
    print("a<b")

#形式四:

x = 1 if a>b else 2
print(x)

 
