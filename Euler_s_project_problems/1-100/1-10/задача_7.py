from math import ceil


def is_prime(num):
    top = int(ceil(num ** 0.5))
    for x in range(3, top + 1, 2):
        if num % x == 0:
            return False
    return True


max = 10001
f = 0
a = 1
perv_chislo = 3
while a < max:
    if is_prime(perv_chislo) is True:
        f = perv_chislo
        print(str(a + 1) + ")", perv_chislo)
        a = a + 1
    perv_chislo += 2
print("______")
print(f)
