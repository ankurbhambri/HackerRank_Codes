n = 6
types = [1,4,4,4,5,6]
count = {}
for t in types:
    if t in count.keys():
        count[t] += 1
    else:
        count[t] = 1


max_value = max(count.values())
required_keys = [k for k, v in count.items() if v == max_value]
print(min(required_keys))
