from tools import relat_prime
from math import ceil

'''
300000/700000
428571/1000000

'''
best=10
x=10**5*2
for c in range(1,1000):
    for f in range(1,x):
        n=(428571+ceil(x/2)-f)
        d=(1000000-c)
        a=(3/7)-n/d
        if 0<a<best and relat_prime(n,d) :
            best=a
            print(n,d,best)

'''best=1
for d in range(1, 10000):
    for n in range(ceil((d*2.5)/7), ceil((d*3)/7)):
        a=3/7-n/d
        if relat_prime(n,d) and a<best:
            best=a
            print(n,d,n/d,best)'''