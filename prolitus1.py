n=int(input('Enter nos :'))
l=[]
count = 0
temp = 0
for i in range(0,n):
    d=int(input('Enter value :'))
    l.append(d)
    
for x in l:
    v=x
    while v!=0:
        temp=v//10
        if temp//x==0 or temp!=0:
            count+=1
        v//=10
        
    print("Divisor of = ",x,"Divisible nos = ",count)
    count=0
        
       

       
           
           
           
