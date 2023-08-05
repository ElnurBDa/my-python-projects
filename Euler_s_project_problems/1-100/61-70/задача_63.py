count=0
for n in range(1,10):
    for power in range(1,30):
        if len(str(n**power))==power:
            count+=1
            print(count,n,power,n**power)





