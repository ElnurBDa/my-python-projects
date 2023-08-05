def is_prime(n):
    if n == 1:
        return False
    from math import ceil
    for x in range(2, ceil(n ** .5) + 1):
        if n % x == 0:
            return False
    return True


def is_odd_composite(n):
    if n % 2 == 0 or is_prime(n):
        return False
    return True


def spec_func(n):
    from math import ceil
    z=n
    for x in range(2, n):
        if is_prime(x):
            z -= x
            z/=2
            z=z**.5
            if ceil(z)==z:
                return n,x,z
            z=n
    return 2


for x in range(2,10000):
    if is_odd_composite(x):
        if spec_func(x)==2:
            print(x)