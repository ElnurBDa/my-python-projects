def func1(x=str):
    if x[0] == "0":
        x = x[1:]
    return eval(x)


file = open("cal.txt","r+")

ftxt = file.read()
a = []
for x in range(0, len(ftxt)):
    if ftxt[x:x + 7] == "DTSTART":
        t = ftxt[x:x + 39]
        if t[7] == ";":
            a.append(t[t.index(":") + 10:t.index("\n") - 2])
        if t[7] == ":":
            a.append(t[t.index(":") + 10:t.index("Z") - 2])
    if ftxt[x:x + 5] == "DTEND":
        t = ftxt[x:x + 37]
        if t[5] == ";":
            a.append(t[t.index(":") + 10:t.index("\n") - 2])
        if t[5] == ":":
            a.append(t[t.index(":") + 10:t.index("Z") - 2])
'''
hour/minute 
'a1a2','a3a4'
'''
a1 = []
a2 = []
a3 = []
a4 = []
for x in range(0, len(a)):
    if x % 2 == 0:
        a1.append(func1(a[x][:2]))
        a2.append(func1(a[x][2:]))
    if x % 2 == 1:
        a3.append(func1(a[x][:2]))
        a4.append(func1(a[x][2:]))

s=sum(a3)-sum(a1)+(sum(a4)-sum(a2))/60
print(s,"hours")
print(s/24,"days")




file.close()
