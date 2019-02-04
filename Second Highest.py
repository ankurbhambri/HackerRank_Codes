a= []
n = int(input("Length of list"))

for i in range(0,n):
    c = int(input("Enter element"))
    a.append(c)
    
a.sort()


print(a[-2]) 

