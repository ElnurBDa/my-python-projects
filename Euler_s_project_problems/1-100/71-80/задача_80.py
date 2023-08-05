from  tools import ok_sqrt


sum=0
bad_nums=[1,4,9,16,25,36,49,64,81,100]
for n in range(1,101):
    if n not in bad_nums:
        s=(str(ok_sqrt(n,200)))[:100]
        for x in s:
            sum+=int(x)

        print(n,s)
print(sum)