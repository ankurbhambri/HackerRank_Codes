def knapsack(arr, W):
    n = len(arr)
    if n == 0 or W==0:
        return 0
    else:
        knapsack(arr, W)

if __name__ == "__main__":
    arr = {1:1, 3: 4, 4: 5, 5:7}
    W = 7
    print(knapsack(arr, W))
