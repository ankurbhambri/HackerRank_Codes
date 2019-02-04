n=[22,22,21,20,20,20,16,15,15]
l=len(n)
d={}
c=0
g=0
count=1

for j in n:   
    if j in d.keys():
        d[j]+=1
    else:
        d[j]=1
        
for k,v in d.items():
    c+=1
    if(v>1):
        g=c
        print(k,g)
        c+=v
        c-=1
    if(v==1):
        print(k,c)
