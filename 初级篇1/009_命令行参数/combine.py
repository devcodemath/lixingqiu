"""combine.py 本程序能合并ANSI文本文件的内容,用法为在命令行输入：
   combine.py 1.txt 2.txt 3.txt 4.txt 5.txt he.txt
   能把1.txt到5.txt的文件合并到he.txt
"""
import sys

def readfile(filename):
    """读文件内容的函数,返回文件的内容"""
    f = open(filename,mode='r')
    fc = f.read()
    f.close()
    return fc

def writefile(filename,filecontent):
    """把文件内容写到filename的函数"""
    f = open(filename,mode='w')
    f.write(filecontent)
    f.close()

if len(sys.argv) < 4:
    print("本程序能合并ANSI编码格式的文本文件。")
    print("用法:\n","combine.py 文件名1 文件名n 合成的文件名")
    sys.exit(0)

files = []

for i in range(1,len(sys.argv)-1):    # 待读取的文件名列表
    files.append(sys.argv[i])
    
outfile = sys.argv[len(sys.argv)-1]   # 获取输出文件名

fc = ""
for file in files:
    filecontent = readfile(file)      # 读一个文件的内容
    fc = fc + filecontent             # 累加所有文件的内容

writefile(outfile,fc)                 # 把所有文件内容写到outfile中
print("已成功合并到文件：",outfile)
