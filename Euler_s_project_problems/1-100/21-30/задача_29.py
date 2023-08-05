a=[]
for x in range(2,101):
    for y in range(2,101):
        a.append(x**y)
a.sort()
i=0
count=0
for x in a:
    i+=1
    try:
        if a[i-1]!=a[i]:
            print(x)
            count+=1
    except:
        print(x)
        count+=1
        print('_________Result________')
        print(count)




