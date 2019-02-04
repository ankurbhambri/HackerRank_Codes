x='10:45:05PM'

t=x.split(':')

if(t[2][2]=='P' or t[2][2]=='p'):
    
    if(t[0]!='12'):
        t[0]=str(12+int(t[0]))
        
    elif(t[0]=='12'):
        t[0]='00'
        
    t=':'.join(t)
    
print (t[:-2:])
