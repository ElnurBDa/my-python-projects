b = 0
c = 1

from math import fmod


def chislo_deliteley(x):
    global f
    a = 1
    f = 0
    while x != 1:
        if fmod(x, a) == 0:
            f = f + 1
            print(f)
        a = a + 1
        if a == x:
            break
    print(f+1)
chislo_deliteley(76576500)

'''for a in range(1, 150000000):
    b = b + a
    chislo_deliteley(b)
    if f + 1 > 500:
        print("______________")
        print(b)
        print(f + 1)
        break'''
#решил но из за того чтоб комп слаб число находилось долго и я восполбзовался слугой инета
