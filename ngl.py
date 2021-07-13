arr = [6, 2, 5, 4, 5, 1, 6]

ngl = []
val = 0
for i in range(len(arr)):
    for j in range(i, -1, -1):
        if arr[i] < arr[j]:
            val = arr[j]
            break
        else:
            val = -1
    if val == -1:
        ngl.append(val)
    else:
        ngl.append(val)

print(ngl)
