SUM=0
for x in range(4000,200000):
    strng=str(x)
    l=len(strng)
    c=0
    sum=0
    while c<l:
        sum+=int(strng[c])**5
        c+=1
    if x==sum:
        print(x,sum)
        SUM+=x
print(SUM)







