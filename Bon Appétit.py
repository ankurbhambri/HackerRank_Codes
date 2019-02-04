n=[3,10,2,9]
k=1
b=12
sum=0
for i in n:
    sum = sum+i
sum=sum-n[k]
print(sum)

if(sum//2==b):
    print("Yes")
else:
    print("No")
