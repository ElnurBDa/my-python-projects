
def is_pif2(a,b,c):
    l=[a,b,c]
    q=max(l)
    l.remove(q)
    if q== l[0]+l[1]:
        return True
    return False

def func_r(A,B):
    return (A[0]-B[0])**2+(A[1]-B[1])**2

q=50
count=0
sET=[]
n=[]
for x in range(0,q+1):
    for y in range(0,q+1):
        sET.append((x,y))
sET.remove((0,0))
for P in sET:
    for Q in sET:

        a=func_r(P,Q)
        b=func_r((0,0),Q)
        c=func_r(P,(0,0))
        if is_pif2(a,b,c) and P!=Q:
            count+=1
            n.append((P,Q))

print(count/2)
print(n)



