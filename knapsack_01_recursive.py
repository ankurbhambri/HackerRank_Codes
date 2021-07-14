def knapSack(W, wt, val, n):
    # Base cndt
    if n == 0 or W==0:
        return 0
    if wt[n-1] > W:
        knapSack(W, wt, val, n-1)
    else:
        return max(
            wt[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1)
        )

if __name__ == "__main__":
    wt = [10, 20, 30]
    val = [60, 100, 120]
    W = 50
    n = len(val)
    print (knapSack(W, wt, val, n))
