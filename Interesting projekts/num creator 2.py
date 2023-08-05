print("Input:(Example:1-10 2-27 35-100 )")
a=input()+' '
b='['
c=[]
for x in a :
    if x=='-':
        b+=','
    elif x == ' ' :
        b+=']'
        c.append(eval(b))
        b='['
    else:
        b+=x
print(c)
for x in c:
    for y in range(x[0],x[1]+1):
        print(str(y)+')\n\n'+'█'*15)
    print()
    print()
    print()
input()