

max=0
digit_sum=0
for a in range(1,100):
    for b in range(1,100):
        for c in str(a**b):
            digit_sum+=int(c)
        if digit_sum>max:
            max=digit_sum
        digit_sum=0

print(max)


