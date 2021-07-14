def subset_sum(arr_set, m_sum):

    n = len(arr_set)

    l =[[False for i in range(m_sum + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        l[i][0] = True

    for i in range(1, m_sum + 1):
         l[0][i]= False

    for i in range(1, n+1):
        for j in range(1, m_sum+1):
            if arr_set[i-1] <= j:
                l[i][j] = (l[i][j-arr_set[i-1]] or l[i-1][j])
            else:
                l[i][j] = l[i-1][j]

    return l[n][m_sum]

if __name__ == "__main__":
    arr_set = [2,3,7,8,10]
    m_sum = 11
    print(subset_sum(arr_set, m_sum))
