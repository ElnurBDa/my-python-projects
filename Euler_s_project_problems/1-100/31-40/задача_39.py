def is_pif(a, b, c):
    lll=[a,b,c]
    q=max(lll)
    lll.remove(q)
    w,r=lll
    if q**2==w**2+r**2:
        return True
    return False



def sol_for_p(p):
    from math import ceil
    lll=[]
    for a in range(1,ceil(p/2)):
        for b in range(1,ceil((p-a)/2)):
            c=p-a-b
            if is_pif(a,b,c) and {a,b,c} not in lll :
                lll.append({a,b,c})
    return lll


a=0
z=0
for x in range(1,1001):
    s=sol_for_p(x)
    print(x,')',len(s),s)
    if len(s)>a:
        a=len(s)
        z=x
print(a,z)
