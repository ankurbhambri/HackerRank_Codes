n=6
v=n
for i in range(0,n):
    for j in range(1,v):
        print(end=' ')
    v=v-1
    for k in range(0,i+1):
        print('# ',end='')
    print('\r')
        

