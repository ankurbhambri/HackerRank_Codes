l=[5,10,25,20,5,4]
v=[]
min = l[0]
max = l[0]
max_count=0
min_count = 0
for x in range(len(l)):
    if(l[x]>max):
        max = l[x]
        max_count+=1
    if(l[x]<min):
        min = l[x]
        min_count+=1
print(max_count,min_count)

        
