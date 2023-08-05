from itertools import permutations
digits=['0','1','2','3','4','5','6','7','8','9']



def is_num_this(ssss):
    if int(ssss[1:4])%2!=0:
        return False
    if int(ssss[2:5])%3!=0:
        return False
    if int(ssss[3:6])%5!=0:
        return False
    if int(ssss[4:7])%7!=0:
        return False
    if int(ssss[5:8])%11!=0:
        return False
    if int(ssss[6:9])%13!=0:
        return False
    if int(ssss[7:10])%17!=0:
        return False
    return True

sum=0
number=''
for x in permutations(digits):
    for a in x :
        number+=a
    if is_num_this(number):
        print(number)
        sum+=int(number)
    number=''
print(sum)

