
a=1
b=1
count=0
for x in range(1,1000):
    a_=2*b+a
    b_=a+b
    a=a_
    b=b_
    print(x,a,b)
    if len(str(a))>len(str(b)):
        count+=1
print(count)








