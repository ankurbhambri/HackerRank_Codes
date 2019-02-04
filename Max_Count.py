l = [3,2,1,3]
n = len(l)
count = 0
m = max(l)
for i in l:
    if m==i:
        count+=1
print(count)
