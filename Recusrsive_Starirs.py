def countWaysUtil(n,m): 
    if n <= 1: 
        return n 
    res = 0
    i = 1
    while i<=m and i<=n: 
        res = res + countWaysUtil(n-i, m) 
        i = i + 1
    return res 
      
# Returns number of ways to reach s'th stair     
def countWays(s,m): 
    return countWaysUtil(s+1, m) 
      
  
# Driver program 
s,m = 4,2
print ("Number of ways =",countWays(s, m)) 
