from  decimal import Decimal,getcontext
size=10000

getcontext().prec=size
D=Decimal


def cyclist(string):
    y=1
    cycle_size=0
    ddd=0
    while y<size:
        if string[0:y]==string[y:2*y] :
            cycle_size=y
            ddd+=1
        y+=1
        if ddd==1:
            return cycle_size, string[0:y]



ass=[]
x=1
while x<1001:
    w=D(1)/D(x)
    q=str(w)
    #Cut
    if q[0:4]=='0.00':
        q = q[4::]
    elif q[0:3]=='0.0':
        q = q[3::]
    elif q[0:2]=='0.':
        q=q[2::]
    if len(q)==size and cyclist(q)!=None  and cyclist(q)[0]!=0 and cyclist(q)[0]!=1:
        ass.append((x,cyclist(q)))

    x+=1

max=(0,(0,0))

for x in ass:
    if x[1][0]>max[1][0]:
        max=x



print(max)
print(D(1)/D(max[0]))

