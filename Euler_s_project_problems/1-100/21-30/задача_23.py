def is_num_abundant(n):
    y = 1
    sum = 0
    while y < n:
        if n % y == 0:
            sum += y
        y += 1
    if n < sum:
        return True


abundants=[]
for x in range(1,28124):
    if is_num_abundant(x):
        abundants.append(x)

print(abundants)
those=[]
for x in range(1,28124):
    count = 0
    for y in abundants:
        if x-y in abundants:
            count+=1
            break
    if count==0:
        those.append(x)
print(those)
sum=0
for s in those:
    sum+=s
print(sum)



