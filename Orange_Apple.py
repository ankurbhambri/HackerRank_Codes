count=0
count1=0
app=[]
orr=[]
apples = [-2,2,1]
oranges = [5,-6]
s=7
t=11
a=5
b=15
    
for k in apples:
    k+=a
    app.append(k)
print(app)

for t1 in app:
    if(t1>=s and t1<=t):
        count+=1

for k in oranges:
    k+=b
    orr.append(k)
print(orr)

for t1 in orr:
    if(t1>=s and t1<=t):
        count1+=1
        
print(count)
print(count1)
