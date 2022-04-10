"""musicwithlrc.py。本程序定义两个函数，返回唱词的毫秒间隔时间和歌词。"""

__author__ = "李兴球"
__date__ = "2019/2/20"

def convert_to_msecond(line):
    """把lrc歌词文件中里中括号里的唱点时间转换成毫秒值，
    即把'[00:05.25]歌词'这样的转换成(650,歌词),以元组形式返回。"""
     
    sentence = line.split("]")[-1]            # 歌词    
    time = line.split("]")[0]                 # 中括号里的时间     
    time = time[1:]                           # 下面把00:10.00这样的转换成毫秒
    items = time.split(".")
    items = [item.strip() for item in items]  # 剥皮处理      
    ps = int(items[-1]) * 10                  # 毫秒 
    time = items[0]                           # 01:33形式的时间
    se = int(time.split(":")[-1]) * 1000      # 秒转换成毫秒
    mi = int(time.split(":")[0]) * 60 * 1000  # 分转换成毫秒
    return (mi + se + ps,sentence)

def make_septime_lrc(lrcfile):
    """生成歌词的间隔时间表，给海龟画图的ontimer用，返回列表，列表中的项目是二元组。
    二元组的内容是歌词显示的时间和歌词。    """
    
    septime_lrc = []                        # 存放每行应该显示的时间和歌词
    fc = []                                 # 存放每一行
    f = open(lrcfile,encoding='utf-8')
    for line in f:
        line = line.strip()
        if len(line)>10:fc.append(line)
    f.close()    
    amounts = len(fc)
    # 第一行的内容，它的歌词显示时间为第二行的时间减去它的时间
    current_items = convert_to_msecond(fc[0])# 唱到当前行的时间和歌词
    for index in range(amounts-1):           # 最后一行不需要显示时间   
        next_line = fc[index+1]              # 下一行文件内容            
        next_items = convert_to_msecond(next_line) # 唱到下一行的时间和歌词
        current_time = current_items[0]      # 唱到此行的毫秒数
        next_time = next_items[0]            # 唱到下一行的毫秒数
        sep = next_time - current_time       # 当前行应该显示的毫秒数
        septime_lrc.append((sep,current_items[1].strip()))
        current_items = next_items 
    return septime_lrc

if __name__ == "__main__":

    lrc_for_ontimer = make_septime_lrc("白桦林.lrc")
    for lrc in lrc_for_ontimer:
        print(lrc)
                            
