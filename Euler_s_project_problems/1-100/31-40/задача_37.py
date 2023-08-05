
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

def func(n):
    str_n=str(n)
    l=len(str_n)
    for x in range(0,l):
        if is_prime(int(str_n[x:]))==False:
            return False
    str_n=str(n)
    for x in range(1,l+1):
        if is_prime(int(str_n[:x]))==False:
            return False
    return True


x=10
count=0
sum=0
while True:
    if func(x):
        print(x)
        sum+=x
        count+=1
    if count==11:
        break

    x+=1


print(sum,count)


