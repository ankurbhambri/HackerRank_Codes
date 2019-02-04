b=10
n=[3,1]
m=[5,2,8]
sum=0
l =[]
v=[]
k=0

for i in n:
    for j in m:
        sum = i+j
        l.append(sum)
for g in l:
    if(g<=b):
        v.append(g)
if len(v)==0:
    print("-1")
else:
    k=max(v)
    print(k)

            
       


        
        
