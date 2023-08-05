from math import factorial

def func(n):
    str_n=str(n)
    sum=0
    for x in str_n:
        sum+=factorial(int(x))
    return sum

sum=0
for y in range(3,200000000):
    if y==func(y):
        print(y)
        sum+=y
print('sum='+str(sum))













