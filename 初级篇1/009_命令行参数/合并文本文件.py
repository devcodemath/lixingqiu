"""把本程序改成能在命令行输入的,假设
   combine.py 1.txt 2.txt 3.txt 4.txt 5.txt he.txt
   能把1.txt到5.txt的文件合并到he.txt
"""
def readfile(filename):
    f = open(filename,mode='r')
    fc = f.read()
    f.close()
    return fc

def writefile(filename,filecontent):
    f = open(filename,mode='w')
    f.write(filecontent)
    f.close()

files = ['1.txt','2.txt','3.txt','4.txt']

fc = ''                           

for file in files:
    filecontent = readfile(file)
    fc = fc + filecontent

writefile("合并的.txt",fc)
