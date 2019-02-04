l = [1,3,2,6,1,2]
n=len(l)
k=3
count=0
count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (l[i]+l[j]) % k == 0:
            count+=1
print(count)
            
        

         
        
    
    
    

