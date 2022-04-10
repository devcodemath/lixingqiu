"""时间戳演示.py"""

import time
begin_time = time.time()
print("起始时间:",begin_time)
while time.time() - begin_time < 10 :
    pass
print("结束时间:",time.time())
