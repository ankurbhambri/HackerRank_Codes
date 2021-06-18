# root method n(√n)
import math


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    if num > 2 and num % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(num))
    for i in range(3, 1 + max_div, 2):
        if (num % i) == 0:
            return False
    return True


for i in range(97, 103):
    x = is_prime(i)
    c += x

print('total nos of prime nos', c)

# Sieve Eratosthenes O(nlog(log(n)))
def Sieve_Eratosthenes(num):

    bol_arr = {i: True for i in range(num + 1)}
    i = 2
    while i * i <= len(bol_arr):
        if bol_arr[i]:
            for jj in range(i + i, num, i):
                bol_arr[jj] = False
        i += 1
    return bol_arr


check_prime = Sieve_Eratosthenes(37)
print('Prime' if check_prime[7] else 'Not Prime')

# Segmented Sieve
def Segmented_Sieve(a, b):
    bool_arr = {i: True for i in range(a, b + 1)}
    i = 2
    while i * i <= b:
        rr = math.ceil(a / i) * i
        print(rr)
        for jj in range(rr, b, i):
            bool_arr[jj] = False
        i += 1
    return bool_arr


print(Segmented_Sieve(22, 51))
