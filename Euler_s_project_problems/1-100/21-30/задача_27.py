def is_prime(num):
    try:
        from math import ceil
        top = int(ceil(num ** 0.5))
        for x in range(3, top + 1, 2):
            if num % x == 0:
                return False
        return True
    except:
        return False


#    a b n
max=(0,0,0)
for a in range(-999,1000):
    for b in range(-1000,1001):
        n=0
        boool = True
        while boool:
            if is_prime(n ** 2 + a * n + b):
                n+=1
            else:
                boool=False
                if n>max[2]:
                    max=(a,b,n)
print(max,max[0]*max[1])
#(-61, 971, 71) -59231







