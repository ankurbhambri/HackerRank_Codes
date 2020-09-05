
def given_array(given_list, n):
    carry = 1 
    for i in reversed(range(n)):

        if (given_list[i] + 1) >= 10:
            given_list[i] = given_list[i] + carry - 10

            if i==0 and given_list[i] == 0:
                given_list.insert(0, 1)
        else:
            given_list[i] += 1
            return given_list

    return given_list

print('Enter the length of Array')
ll = int(input())

val = [int(input()) for k in range(ll)]
print('Your array', val)

# Output
print(given_array(val, ll))