arr = [100, 80, 60, 70, 60, 75, 85]

ssp = []

for i in range(len(arr)):
    count = 0
    for j in range(i, -1, -1):
        if arr[i] >= arr[j]:
            count += 1
        else:
            break
    ssp.append(count)
print(ssp)
