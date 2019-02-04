a=[4,6,5,3,3,1]
maximum = 0
diff = 1

for k in a:
    n1 = a.count(k)

    
    n2 = a.count(k-diff)
 
    maximum = max(maximum, n1+n2)
    print(n1,n2,n1+n2)
    
   
    
print(maximum)

       

