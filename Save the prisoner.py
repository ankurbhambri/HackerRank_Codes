p=7
t=19
k=2
l=[]
for i in range(t):
    if(k<=p):
        l.append(k)
        k+=1
    if(k==p+1):
        k=1
        l.append(k)
        k+=1    
print(l[t-1])



""" or hackerrank solution is 
l = (s - 1 + m) % n
    if l == 0:
        l = n
    return l """
    

        
        
    
