l = [2, 5 ,1 ,3 ,4 ,4 ,3 ,5 ,1 ,1 ,2 ,1 ,4 ,1 ,3 ,3 ,4 ,2, 1]
n=len(l)
sum=0
m=7

v=1
t=m
d=18

count=0

print(l,'\n')


for i in range(0,n):
    
    sum=l[i]
    print('value at l[i]',l[i],'range of i',i)
    
    for j in range(v,t):
        if(t<=n):
            sum+=l[j]
            print('value at l[j]',l[j],'range of j',j,'With v,m',v,t)
        
    if(sum==d):
        count+=1
        
        print('Sum when count is incremented',sum)
        print('Count',count)

        
    
    v+=1
    t+=1
    
print('Final count',count)

            
        

         
        
    
    
    

