"""本程序安装coloradd.py模块到python安装文件夹的lib目录中
   需要事先安装python3，否则无法运行。作者：李兴球 """
import shutil
import sys 
import os 

src="coloradd.py"
dst=sys.prefix + "\\Lib\\"
 
print("本程序复制 coloradd.py 到 python的模块库文件夹中。")
print("目标文件夹：" + dst)
print()
print("                      作者：李兴球，QQ:406273900。")
print()

if not os.path.exists(src):
    print("很疑憾，没有找到 'coloradd.py' 文件。")
else:        
    try: 
        #复制 
        shutil.copy(src, dst)
        print("提示:","复制成功！")     
    except PermissionError:
        print("由于你对目标文件夹没有写入权限，请人工复制'coloradd.py'到目标文件夹。")        
    except:
        print("提示:","复制失败！原因未知。")
os.system("explorer.exe " + dst)    
input()
