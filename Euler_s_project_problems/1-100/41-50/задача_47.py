from time import time

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    from math import ceil
    top = int(ceil(num ** 0.5))
    if num % 2 == 0:
        return False
    for x in range(3, top + 1, 2):
        if num % x == 0:
            return False
    return True


def func(n):
    y = 1
    delivers = []
    while y < n / 2 + 1:
        if n % y == 0 and is_prime(y) and y not in delivers:
            delivers.append(y)
        y += 1
    return len(delivers)

start=time()
file = open('problem_47.txt', 'w')
file.write('20:38')
file.close()
x = 1
while True:
    x += 1
    if func(x) == func(x + 1) == func(x + 2) == func(x + 3) == 4:
        print(x,time())
        file = open('problem_47.txt', 'w')
        file.write((str(x)+'   '+str(time()-start)))
        file.close()
        break
