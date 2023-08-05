from tools import relat_prime
from math import ceil,floor




count=0
p=0.000000000000001
for d in range(1, 12001):
    for n in range(ceil(d/3+p), ceil(d/2-p)):
        a=3/7-n/d
        if relat_prime(n,d) :
            count+=1
print(count)