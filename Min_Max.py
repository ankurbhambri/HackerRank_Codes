arr = [4,3,1,5,2]

maxx = max(arr)
minn = min(arr)

maxi = arr.copy()
maxi.remove(minn)



mini = arr.copy()
mini.remove(maxx)




sum_max = sum(maxi)
sum_min = sum(mini)

print(sum_max,sum_min)
