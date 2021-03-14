arr = [6, 2, 5, 4, 5, 1, 6]
ngr = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] < arr[j]:
            if arr[i] == 1:
            next = arr[j]
            break
        else:
            next = -1
    if next == -1:
        ngr.append(next)
    else:
        ngr.append(next)

print(ngr)
