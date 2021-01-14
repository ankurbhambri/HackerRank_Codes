js = ['10101', '11100', '11010', '00101']
lp = {}

for i in range(len(js)-1):
    for j in range(i+1, len(js)):
        lp[str(i)+','+str(j)] = []
        aa = []
        for k in range(len(js[i])):
            if js[j][k] == '1' or js[i][k] == '1' or (js[j][k] == '1' and js[i][k] == '1'):
                aa.append(1)
            else:
                aa.append(0)
        lp[str(i)+','+str(j)] = aa
        aa = []
        print(i, j)


for i, j in lp.items():
    lp[i] = sum(j)
ans = [k for k, v in lp.items() if v==max(lp.values())]
print(max(lp.values()), len(ans))



# or 


def solution():
    res = 0
    cnt = 0
    for ind in range(len(js)-1):
        for jnd in range(ind+1, len(js)):
            tmp = bin(int(js[ind], 2) | (int(js[jnd], 2))).count("1")
            if tmp > res:
                res = tmp
                cnt = 1
            elif tmp == res:
                cnt += 1

    return (res, cnt)