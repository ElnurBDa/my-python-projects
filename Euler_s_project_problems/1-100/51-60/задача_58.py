
'''
|43|44|45|46|47|48|49|
|42|21|22|23|24|25|26|
|41|20| 7| 8| 9|10|27|
|40|19| 6| 1| 2|11|28|
|39|18| 5| 4| 3|12|29|
|38|17|16|15|14|13|30|
|37|36|35|34|33|32|31|

1,25,101,261
1,+2,+4,+6,

1x1-0
3x3-1
5x5-2
7x7-3
9x9-4

2*n+1=1001
n=500
'''


def is_prime(n):
    if n == 1:
        return False
    elif n==2:
        return True
    from math import ceil
    for x in range(2, ceil(n ** .5) + 1):
        if n % x == 0:
            return False
    return True


primes=[]
k=0
y=1
x=1

while x:
    for z in range(1,5):
        k+=y
        y+=2*x
        if is_prime(y):
            primes.append(y)
    print(2*x+1,x*4+1,len(primes),'    ',len(primes)/(x*4+1))
    if len(primes)/(x*4+1)<.1:
        print(2*x+1)
        break
    x+=1
#26241