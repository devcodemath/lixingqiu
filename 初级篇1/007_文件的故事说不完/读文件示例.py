"""读文件示例.py"""

filename = "fish.txt"
f = open(filename,mode='r')
fc = f.read()
f.close()
print(fc)
