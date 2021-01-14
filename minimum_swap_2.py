# arr = [7, 1, 3, 2, 4, 5, 6]
# steps = 0
# for i in range(len(arr)):
#     min_val = min(arr[i:len(arr)])
#     pos = arr.index(min_val)
#     if min_val < arr[i]:
#         arr[pos], arr[i] = arr[i], min_val
#         steps += 1

# print(arr, steps)



def minimumSwaps(arr):
    swaps = 0
    n = len(arr)
    import ipdb; ipdb.set_trace()
    for idx in range(n):
        while arr[idx]-1 != idx:
            ele = arr[idx]
            arr[ele-1], arr[idx] = arr[idx], arr[ele-1]
            swaps += 1
    return swaps

arr = [7, 1, 3, 2, 4, 5, 6]
minimumSwaps(arr)