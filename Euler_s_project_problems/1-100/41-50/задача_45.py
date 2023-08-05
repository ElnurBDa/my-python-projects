limit=100000
tr=[]
for x in range(1,limit):
    tr.append(x*(x+1)/2)

pn=[]
for x in range(1,limit):
    pn.append(x*(x*3-1)/2)

hx=[]
for x in range(1,limit):
    hx.append(x*(x*2-1))






for x in hx:
    if x in tr and x in pn and x>40750:
        print(x)

#1533776805







