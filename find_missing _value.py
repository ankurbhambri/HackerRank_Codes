ll = [1, 2, 2, 2, 4, 5, 7, 8, 9, 11, 12, 14, 20, 16, 18, 25, 3, 3, 30, 22, 22]
lv = []

n = max(ll)

for i in range(1, n):
    lv.append(i)

vv = set(lv) - set(ll)