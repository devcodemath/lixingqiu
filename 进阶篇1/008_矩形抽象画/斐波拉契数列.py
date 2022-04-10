"""斐波拉契数列"""

def fibo(n):
    if n == 1 or n==2 :
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(1,10):
    print(fibo(i),end=' ')
