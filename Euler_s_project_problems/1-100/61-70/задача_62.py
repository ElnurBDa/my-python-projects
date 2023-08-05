cubes = []
for x in range(1, 10001):
    cubes.append(str(x ** 3))
specubes = []
epicspecubes = []
l = len(cubes[-1])
for i in range(0, l):
    specubes.append([])
    epicspecubes.append([])
    for x in cubes:
        if len(x) == i + 1:
            specubes[i].append(x)

for i in range(0, l):
    for x in specubes[i]:
        epicspecubes[i].append(sorted(x))

for x in epicspecubes:
    for y in x:
        if x.count(y)==5:
            print(y,x.index(y) )

print(specubes[11][385])
print(specubes[11][554])
