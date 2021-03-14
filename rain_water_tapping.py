def max_left(arr):
    maxl = []
    first = arr[0]
    for i in range(len(arr)):
        if first < arr[i]:
            first = arr[i]
        maxl.append(first)
    return maxl

def max_right(arr):
    maxr = []
    last = arr[-1]
    for i in range (len(arr)):
        if last < arr[-i]:
            last = arr[-i]
        maxr.append(last)
    return maxr

if __name__ == "__main__":
    arr = [3, 0, 0, 2, 0, 4]
    a1 = max_left(arr)
    a2 = max_right(arr)
    water = 0
    for i in range(len(arr)):
        water += min(a1[i], a2[i]) - arr[i]
    print(water)

''' like 
    arr =  3, 0, 0, 2, 0, 4
max left: >3  3  3  3  3  4 
max right: 4  4  4  4  4  4<
min =      3  3  3  3  3  4
water cap  3  0  0  2  0  4
ans        0  3  3  1  3  0
'''

