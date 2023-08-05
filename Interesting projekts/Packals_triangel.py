l = int(input('Enter level size : '))
a = []

for x in range(l):
    a.append([0] * l)

for x in a:
    x[0] = 1
for x in a:
    for y in range(1, l):
        for z in range(1, l):
            a[y][z] = a[y - 1][z - 1] + a[y - 1][z]

w=0
for x in a:
    for y in x:
        w+=1
        if y!=0:
            print(y,end=' ')
        if w==l:
            print('\n')
            w=0

