import sys

p = sys.argv
 
if len(p) < 3 :
    print("参数太少")
else:
    print(int(p[1]) + int(p[2]))
