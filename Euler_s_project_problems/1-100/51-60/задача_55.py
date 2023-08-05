from time import time
start=time()


def is_polindrom(string):
    l=len(string)
    if l%2==0:
        if string[0:l]==string[l::-1]:
            return True
        else:
            return False
    else:
        if string[0:l]==string[l+1::-1]:
            return True
        else:
            return False

def is_lychrel(n):

    num=n
    for x  in range(50):
        num+=int(str(num)[::-1])
        if is_polindrom(str(num)):
            return False
    return True

count=0
for x in range(1,10001):
    if is_lychrel(x):
        count+=1
        print(x)
print(count,time()-start)
#249









