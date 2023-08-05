def timer(func):
    def func_wrapper(*args, **kwargs):
        from time import time
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        time_spend = time_end - time_start
        print('%s cost time: %.3f s' % (func.__name__, time_spend))
        return result
    return func_wrapper

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def phi(n):

    return sum([1 for x in range(2,n) if gcd(x,n)==1])+1

def arePermutation1(a,b):
    a=str(a)
    b=str(b)

    if len(a)!=len(b):return False

    count_a=[0]*10
    count_b=[0]*10

    for i in a:
        count_a[int(i)]+=1
 
    for i in b:
        count_b[int(i)]+=1

    for i in range(10):
        if count_a[i]!=count_b[i]:return False

    return True

def arePermutation2(a,b):
    a=str(a)
    b=str(b)
    l=len(a)

    if l!=len(b):return False

    count=[0]*10

    for i in range(l):
        count[int(a[i])]+=1
        count[int(b[i])]-=1

    for x in count:
        if x!=0: return False

    return True

from sympy import isprime

