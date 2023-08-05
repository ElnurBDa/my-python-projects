from math import ceil


def is_prime(num):
    top = int(ceil(num ** 0.5))
    for x in range(3, top + 1, 2):
        if num % x == 0:
            return False
    return True


max=2000000
sum=2
perv_chislo = 3
while perv_chislo < max:
    if is_prime(perv_chislo) is True:
        sum=sum+perv_chislo
    perv_chislo += 2
print(sum)
