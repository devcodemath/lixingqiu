"""计算从1到100自然数的和"""

def zsum(number):
    if number == 1:
        return number
    else:
        return zsum(number - 1)  + number

print(zsum(100))
