from itertools import combinations

def pairs(k, arr):
    comb = list(combinations(arr, 2))
    pairs = list(filter(lambda x: abs(x[1] - x[0]) == k, comb))
    return len(pairs)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(str(result))

    # fptr.write(str(result) + '\n')

    # fptr.close()
