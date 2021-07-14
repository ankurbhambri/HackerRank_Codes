def lcs(str1, str2, n, m):
    print(n,m)
    if n == 0 or m == 0:
        return 0
    elif str1[n-1] == str2[m-1]:
        print('match', n-1, m-1)
        return 1 + lcs(str1, str2, n-1, m-1)
    else:
        return max(lcs(str1, str2, n, m-1), lcs(str1, str2, n-1, m))

if __name__ == "__main__":

    str1 = "Ankur"
    str2 = "Ankit"
    print(lcs(str1, str2, len(str1), len(str2)))
