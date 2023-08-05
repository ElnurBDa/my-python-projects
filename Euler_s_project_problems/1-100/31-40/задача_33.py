

a=[]
for x in range(10,100):
    for y in range(10,100):
        x1=int(str(x)[0])
        x2=int(str(x)[1])
        y1=int(str(y)[0])
        y2=int(str(y)[1])
        if x2!=0 and y2!=0 and ((x1!=y2 and x2==y1 and x1/y2==x/y) or (x2!=y1 and x1==y2 and x2/y1==x/y)) and x<y:
            a.append((x,y))


X=1
Y=1
for x in a:
    X*=x[0]
    Y*=x[1]

print(X,Y)