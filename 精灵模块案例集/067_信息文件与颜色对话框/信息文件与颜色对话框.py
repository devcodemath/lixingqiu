"""
   询问及文件与颜色对话框
"""
from sprites import *

screen = Screen()

if  askyesno('询问','请按是或否'):
    showinfo('信息','你按了是')
else:
    showinfo('信息','你按了否')

showwarning('警告','玩火必自焚')
showerror('错误','有个bug等你清除')

ret = askquestion('提问','明天买腊肉吗?')
if ret == 'yes':
    showinfo('信息','过年当然要买腊肉')
else:
    showinfo('信息','今年肉价好贵,吃不起腊肉了')

if  askokcancel('信息','确定?'):
    showinfo('信息','按了确定')
else:
    showinfo('信息','按了取消')

ret = askyesnocancel('信息','确定、否、取消')
if ret == True:
    showinfo('信息','你按了确定')
elif ret == False:
    showinfo('信息','你按了否')
else:
    showinfo('信息','你按了取消')

if askretrycancel('重试','再试一次？'):
    showinfo('信息','你按了重试')
else:
    showinfo('信息','你按了取消')

options = {}
options['title'] = '请选择一个文件_Python sprites module'
options['filetypes'] = [ ("Python files", "*.py *.pyw", "TEXT"),
                       ("Text files", "*.txt", "TEXT"),
                       ("All files", "*")]
options['defaultextension'] = '.py' if sys.platform == 'darwin' else ''
options['initialdir'] = 'C:\\Users\Administrator'
options['initialfile'] = '风火轮编程.py'

# 打开一个文件
filename = askopenfilename(**options)
print(filename)

# 试图打开很多文件
options['title'] = '请选择很多文件_Python sprites module'
filenames = askopenfilenames(**options)
print(filenames)

options['title'] = '另存为文件_Python sprites module'
filename = asksaveasfilename(**options)
print('保存的文件名为',filename)

mulu = askdirectory(initialdir='d:')
print('所选择的文件夹为：',mulu)

color = askcolor()
print('选择的颜色为',color)
screen.mainloop()

