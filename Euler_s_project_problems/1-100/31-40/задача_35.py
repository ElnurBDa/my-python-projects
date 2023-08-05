from math import ceil


def is_prime(num):
    top = int(ceil(num ** 0.5))
    if num % 2 == 0:
        return False
    for x in range(3, top + 1, 2):
        if num % x == 0:
            return False
    return True


def is_crucial(n):
    str_n = str(n)
    for x in range(1, len(str_n) + 1):
        if is_prime(int(str_n)) == False:
            return False
        str_n = str_n[1:] + str_n[0]
    return True

count=1
for x in range(2, 1000000):
    if is_crucial(x):
        print(x)
        count+=1
print(count)
