a=[1,2,3]
k=2
queries=[0,1,2]

new_arr = a[-k%len(a):] + a[:-k%len(a)]
result = []

for i in queries:
    result.append(new_arr[i])
    print(result)
    
    
