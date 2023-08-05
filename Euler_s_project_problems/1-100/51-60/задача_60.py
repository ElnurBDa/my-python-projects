def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


olprimes = []
for x in range(2, 1000):
    if is_prime(x):
        olprimes.append(str(x))
print('olprimes are ready')

for x1 in olprimes:
    for x2 in olprimes[olprimes.index(x1) + 1::]:
        if is_prime(int(x1 + x2)) and is_prime(int(x2 + x1)):
            for x3 in olprimes[olprimes.index(x2) + 1::]:
                if is_prime(int(x1 + x3)) and is_prime(int(x2 + x3)) and is_prime(int(x3 + x2)) and is_prime(
                        int(x3 + x1)):
                    for x4 in olprimes[olprimes.index(x3) + 1::]:
                        if is_prime(int(x1 + x4)) and is_prime(int(x2 + x4)) and is_prime(int(x3 + x4)) and is_prime(
                                int(x4 + x3)) and is_prime(int(x4 + x2)) and is_prime(int(x4 + x1)):
                            for x5 in olprimes[olprimes.index(x4) + 1::]:
                                if is_prime(int(x1 + x5)) and is_prime(int(x2 + x5)) and is_prime(
                                        int(x3 + x5)) and is_prime(int(x4 + x5)) and is_prime(
                                    int(x5 + x4)) and is_prime(int(
                                    x5 + x3)) and is_prime(int(x5 + x2)) and is_prime(int(x5 + x1)):
                                    print(x1, x2, x3, x4, x5)
# =>13 5197 5701 6733 8389
