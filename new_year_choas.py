arr = [2, 1, 5, 3, 4]
total_bribes = 0
swaps = 1

for index, item in enumerate(arr):
    if item > index + 3:
        print("Too chaotic")

for i in range(len(arr)):
    for k in range(len(arr)-1):
        if arr[k] > arr[k+1]:
            total_bribes += 1
            arr[k], arr[k+1] = arr[k+1], arr[k]
print(total_bribes)
