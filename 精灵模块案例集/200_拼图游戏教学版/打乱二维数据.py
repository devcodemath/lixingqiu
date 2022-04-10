from random import randint


def shuffle(array):
    rows = len(array)
    cols = len(array[0])
    for _ in range(5):
        i = randint(0,rows-1)
        j = randint(0,cols-1)
        r = randint(0,rows-1)
        c = randint(0,cols-1)
        if (i,j)!=(r,c):
            tmp = array[i][j]
            array[i][j] = array[r][c]
            array[r][c] = tmp

nums = [[1,2,3],
        [4,5,6],
        [7,8,9]]
shuffle(nums)
for row in nums:
    print(row)
