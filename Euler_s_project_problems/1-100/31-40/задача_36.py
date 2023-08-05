
def is_polindrom(string):
    l=len(string)
    if l%2==0:
        if string[0:l]==string[l::-1]:
            return True
        else:
            return False
    else:
        if string[0:l]==string[l+1::-1]:
            return True
        else:
            return False

def _10_to_2(n):
    return str(bin(n)[2:])


sum=0
for x in range(1,1000001):
    if is_polindrom(str(x)) and is_polindrom(_10_to_2(x)):
        print(x,'   |   ',_10_to_2(x))
        sum+=x
print(sum)








