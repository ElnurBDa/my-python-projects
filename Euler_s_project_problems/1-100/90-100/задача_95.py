from tools import  divisors


def func(n):
    return sum(divisors(n))-n

def func2(n):
    a = func(n)
    c=0
    while True:
        a=func(a)
        c+=1
        if a==n:
            return c
        if c>30:
            return False


#27 14316
max=0
f=0
for x in range(1,1000001):
    r=func2(x)
    if r>max:
        max=r
        f=x
        print(r,x)

print(max,f)



