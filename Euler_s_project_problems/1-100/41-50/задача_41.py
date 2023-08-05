

def is_prime(num):
    if num==2:
        return True
    if num ==1:
        return False
    from math import ceil
    top = int(ceil(num ** 0.5))
    if num % 2 == 0:
        return False
    for x in range(3, top + 1, 2):
        if num % x == 0:
            return False
    return True




import itertools


www=['1','2','3','4','5','6','7']
str=''


for x in itertools.permutations(www):
    for a in x:
        str+=a
    if is_prime(int(str)):
        print(str)
    str=''



