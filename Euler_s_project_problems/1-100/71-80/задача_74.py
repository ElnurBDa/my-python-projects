from tools import Sotfoid
s=Sotfoid.sotfoid
'''from itertools import permutations
for x in permutations('9407'):
    a=''
    for y in x:
        a+=y
    a=int(a)
    print(a,s(a))
    Sotfoid.count = 0
    Sotfoid.library = []'''




count=0
for x in range(1,1000000):
    sss=s(x)
    Sotfoid.count = 0
    Sotfoid.library = []
    if sss==60:
        count+=1
print(count)


