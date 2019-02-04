a= [17,28,30]
b = [99,16,8]
n=len(a)
count =0
count1=0

for i in range(0,n):
    if(a[i]>b[i]):
        count = count+1
    elif(a[i]<b[i]):
        count1=count1+1
    else:
        count = count
        count1=count1
        
print(count,count1)
        
