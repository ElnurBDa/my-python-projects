

def cutter(n):
    digits=['1','2','3','4','5','6','7','8','9']
    n_str=str(n)
    if  n_str.count('0')>0:
        return False
    for x in digits:
        if n_str.count(x)>1 :
            return False
    return True


def cutter2(n):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    l=len(n)
    for x in digits:
        if x not in n :
            return False
    return True




def delivers(n):
    y=1
    delivers=[]
    while y<n/2+1:
        if n%y==0:
            delivers.append(y)
        y+=1
    return delivers


def is_pandital(n):
    if cutter(n):
        delivrs=delivers(n)
        for d in delivrs:
            str_d1=str(d)
            str_d2=str(int(n/d))
            string=str(n)+str_d1+str_d2
            if cutter(string) and cutter2(string):
                return True
    return False


sum=0
for n in range(1000,10000):
    if is_pandital(n):
        print(n)
        sum+=n
print(sum)






