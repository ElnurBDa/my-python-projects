def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def phi(n):
	return sum([1 for x in range(2,n) if gcd(x,n)==1])+1

for n in range(1,3001):
	if n/phi(n)>4.5:
		print("{:4f}".format(n/phi(n)),"|{:4}".format(n),":",*[x for x in range(1,n) if gcd(x,n)==1])

print(510510/phi(510510))