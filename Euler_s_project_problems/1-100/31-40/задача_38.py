
def is_pandigital(n):
    digits=['1','2','3','4','5','6','7','8','9']
    for x in digits:
        if x not in n:
            return False
    return True


for x in range(1,100000):
    n=1
    ster = ''
    while True:
        ster +=str(n*x)
        if len(ster )>9:
            break
        if is_pandigital(ster):
            print(x,n,ster)
        n+=1

