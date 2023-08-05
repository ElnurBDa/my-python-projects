from math import factorial
value=1000000
count=0
f=factorial
for n in range(1,101):
    for r in range(1,n+1):
        if f(n)/(f(r)*f(n-r))>value:
            count+=1
            print(count,'  ',n,r)


