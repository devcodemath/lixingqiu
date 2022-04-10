"""结构化时间对象演示.py"""
import time

while True:
    cut = time.time()
    current = time.localtime(cut) # 获取结构化时间对象
    year = current.tm_year       # 获取年份        
    month = current.tm_mon       # 获取月份
    day = current.tm_mday        # 获取日子
    hour = current.tm_hour       # 获取小时
    minute = current.tm_min      # 获取分钟
    second = current.tm_sec      # 获取秒数
    print(year,month,day,hour,minute,second)
    time.sleep(1)
