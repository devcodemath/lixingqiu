
s = 'ABC'
for c1 in s:
    for c2 in s:
        for c3 in s:
            print("".join([c1,c2,c3]),end = ',') # 用 + 号速度更慢
        print()
