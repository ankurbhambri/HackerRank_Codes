# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    value=0
    value1=0
    value2=0
   
    n=len(arr)
    
    for i in arr:
        if(i>0):
            pos=pos+1
        elif(i<0):
            neg=neg+1
        else:
            zero=zero+1
            
    value = pos/n
    value1 = neg/n
    value2 = zero/n
    print( format(value, '.6f'))
    print( format(value1, '.6f'))
    print( format(value2, '.6f'))

    
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    

    plusMinus(arr)

