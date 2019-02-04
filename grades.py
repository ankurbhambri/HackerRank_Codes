l = [44,84,94,21,0,18,100,18,62,30,61,53,0,43,2,29,53,61,40,14,]
    #[45,85,95,21,0,18,100,18,62,30,61,55,0,45,2,29,55,61,40,14,]
v=[]
n=5
t = 10
count=0
    
for i in l:      
    if(i<40 and i>37):
        if(i%n==0):
            v.append(i)
        else:
            i=i+2
            if(i%n==0):
                v.append(i)
            elif(i%n!=0):
                i=i-2
                i=i+1
                if(i%n==0):
                    v.append(i)
                else:
                    i=i-1
                    v.append(i)
            
            
    elif(i>40):
        if(i%n==0):
            v.append(i)
        else:
            i=i+2
            if(i%n==0):
                v.append(i)
            
            elif(i%n!=0):
                i=i-2
                i=i+1
                if(i%n==0):
                    v.append(i)
                else:
                    i=i-1
                    v.append(i)
            
                    
    else:
        v.append(i)
           
                


print(v)
            
            
    
       
        
