#By Badalov Elnur


a=[]
for x in range(0,3):
    a.append([])
for x in range(0,3):
    for y in range(0,3):
        a[x].append(" ")
print(a)
'''
0|1|2
3|4|5
6|7|8

00 01 02
10 11 12
20 21 22

00 10 20
01 11 21
02 12 22

00 11 22
02 11 20

'''



d=0
X='X'
O='O'
x_won=False
o_won=False
xset=[]
oset=[]
while True:
    d+=1
    print("===============")
    for q in a:
        for w in q:
            print(w,end='|')
        print()
        print("------")
    x,y=map(int,input("x y").split())
    if d%2==1:
        a[x][y]=X
    else:
        a[x][y]=O

        
    for i1 in range(0,3):    
        for i2 in range(0,3):
            if a[i1][i2]==X:
                xset.append(str(i1)+str(i2))
            if a[i1][i2]==O:
                oset.append(str(i1)+str(i2))
    sset=xset
    if ('00' in sset and '01' in sset and '02' in sset) or ('10' in sset and '11' in sset and '12' in sset) or ('20' in sset and '21' in sset and '22' in sset) or ('00' in sset and '10' in sset and '20' in sset) or ('01' in sset and '11' in sset and '21' in sset)  or ('02' in sset and '12' in sset and '22' in sset) or ('00' in sset and '11' in sset and '22' in sset) or ('02' in sset and '11' in sset and '20' in sset):
        print("X won!!")
        break
    sset=oset
    if ('00' in sset and '01' in sset and '02' in sset) or ('10' in sset and '11' in sset and '12' in sset) or ('20' in sset and '21' in sset and '22' in sset) or ('00' in sset and '10' in sset and '20' in sset) or ('01' in sset and '11' in sset and '21' in sset)  or ('02' in sset and '12' in sset and '22' in sset) or ('00' in sset and '11' in sset and '22' in sset) or ('02' in sset and '11' in sset and '20' in sset):
        print("O won!!")
        break

    
    
    
    

