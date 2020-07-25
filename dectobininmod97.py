name = int(input())  
concat_val = '' 
 
def mod(a):   
    m = 1000000007  
    return (a%m + m) % m   
 
def binarytodecimal(n):  
    return int(n,2)  
  
def Decimal(name):  
    return bin(name).replace("0b", "")  
  
for i in range(1, name+1):  
    aa = Decimal(i)  
    concat_val += aa  
 
bin_to_dec = binarytodecimal(concat_val) 
print(mod(bin_to_dec), bin_to_dec) 
