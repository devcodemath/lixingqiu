"""add2.py 本程序接受命令行参数,把它们的和累加起来"""
import sys

p = sys.argv
amounts = len(p)
if amounts < 3 :
    print("参数太少")
else:
    s = 0
    for i in range(1,amounts):
        s = s + int(p[i])
    print(s)
