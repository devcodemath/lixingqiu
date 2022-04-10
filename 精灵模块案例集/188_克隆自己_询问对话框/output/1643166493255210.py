import os
import sys
import time
import random
from sprites import askyesno

def filename():
    return  str(time.time()).split('.')[0] + str(random.randint(100000,999999)) + ".py"
    
if askyesno('将生成2个文件,需要生成吗? ','')==True:
    self = sys.argv[0]
    outfld = os.getcwd() + os.sep + 'output'
    if not os.path.exists(outfld):os.mkdir(outfld)

    f = open(self,encoding='utf-8')
    c = f.read()
    f.close()

    for i in range(2):
        fn = outfld + os.sep + filename()
        f = open(fn,mode='w',encoding='utf-8')
        f.write(c)
        f.close()
