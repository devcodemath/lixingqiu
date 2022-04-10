lb = ["华夏","中华","编程娃娃","Python","Scratch"]
f = open("列表.txt",mode='w')
for item in lb:
    f.write(item + "\n")
f.close()


lb2 = []
f = open("列表.txt",mode='r')
for line in f:
    lb2.append(line.strip())
f.close()
print(lb2)
