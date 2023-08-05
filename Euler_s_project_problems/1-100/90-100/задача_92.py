

def func1(n):
    sum=0
    for x in str(n):
        sum+=int(x)**2
    if sum==1:
        return 1
    elif sum==89:
        return 89
    return func1(sum)


count=0

limit=10**7
x=1
while x <=limit:
    if func1(x)==89:
        count+=1
    x+=1
print(count)
