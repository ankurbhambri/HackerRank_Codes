arr = [1, 1, 0, 1, 0]


i = 0
j = len(arr) -1

while i < j:
    print(i, j)
    print(arr)
    if arr[i] == 1:
        arr[i], arr[j] = arr[j], arr[i]

        j -= 1
    else:
        i += 1
print(arr)
