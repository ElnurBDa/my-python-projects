from math import ceil
from itertools import permutations ,combinations



def is_prime(num):
    top = int(ceil(num ** 0.5))
    if num == 1:
        return False
    if num==2:
        return True
    for x in range(2, top + 1, 2):
        if num % x == 0:
            return False
    return True


b=[]
a=[]
num=''
for x in range(1000,10000):
    for y in permutations(str(x)):
        for z in y:
            num+=z

        if is_prime(int(num)) and int(num) not in a and len(str(int(num)))==4:
            a.append(int(num))

        num=''
    if len(a) >= 3:
        a.sort()
        b.append(a)
    a=[]


w=[]
for x in b:
    for y in combinations(x,3):
        r=max(y)
        e=min(y)
        for q in y:
            if r>q>e:
                if r+e==2*q and len(str(r-q))==4 and y not in w:
                    w.append(y)

for x in w :
    print(x)












