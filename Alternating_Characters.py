t = int(input())
for _ in range(t):
    spp = input()
    count = 0
    for i in range(1,len(spp)):
        if spp[i] == spp[i-1]:
            print('spp[i]', spp[i], 'spp[i-1]', spp[i-1])
            print('i', i, 'i-1', i-1)
            count += 1
    print(count)