l=[[4,8,2],[4,5,7],[8,1,5]]
sum=0
sum1=0
n=len(l)
v=[]
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            sum+=l[i][j]    
        if(i==n-j-1):
            sum1+=l[i][j]
v.append(sum)
v.append(sum1)          
        
        

        
           
        

print(v)
