"""copyfile.py 复制文件程序"""
file = 'star.mp4'

f = open(file,mode='rb')
filecontent = f.read()
f.close()
print(type(filecontent))

f = open('star2.mp4',mode='wb')
f.write(filecontent)
f.close()
