"""统计英文单词频率.py"""

separators = ['\n','?','.',',',"’",'-',"“","”",")","(",":","/","–"," "]

f = open("文章.txt")                  # 打开文件 
file_content = f.read()               # 读取内容
f.close()                             # 关闭文件

for sep in separators:
    word_list = file_content.split(sep)  # 分隔文章,形成列表
    file_content = "".join(word_list)    # 连接列表,形成文章

word_set = set(word_list)                # 去除重复的数据
 
freq = dict()
freq = freq.fromkeys(word_set,1) # 新建字典,键为word_set的数据,值都为1
 
for word in word_list:
    freq[word] = freq[word] + 1  # 词频+1
    
def pick(s):                     # 定义函数
    return s[1]

sorted_list = sorted(freq.items(),key=pick) # 按序列中元组的第2个数据的值排序
print(sorted_list)
input()
