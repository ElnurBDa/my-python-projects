
def digits(n):
    a=[]
    for x in str(n):
        a.append(int(x))
    return a


limit=10**7
for x in range(1,limit):
    y1=digits(x)
    y1.sort()
    y2=digits(x*2)
    y2.sort()
    y3=digits(x*3)
    y3.sort()
    y4=digits(x*4)
    y4.sort()
    y5=digits(x*5)
    y5.sort()
    y6=digits(x*6)
    y6.sort()
    if y1==y2==y3==y4==y5==y6:
        print(x,x*2,x*3,x*4,x*5,x*6)












