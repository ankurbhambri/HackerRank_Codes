a=[10,20,20,10,10,30,50,10,20]
count=0
d={}
g=[]
t=0
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1


for k,v in d.items():
    g.append(v)
for i in g:
    if i>=2:
        v=i//2
        t=t+v
print(t)
        
        
    
        
