while True:
	print('n from a goes to b')
	n=int(input(('n= ')))
	a=int(input(('a= ')))
	b=int(input(('b= ')))



	def n_from_a_to_b(n,a,b):
		sn=str(n)
		l=len(sn)
		n_in10=0
		for y in range(0,l):
			if int(sn[y])>=a:
				return sn[y]+'>='+str(a)
			n_in10+=int(sn[y])*(a**(l-y-1))
		n_in_b=''
		while n_in10!=0:
			r=n_in10%b
			n_in_b+=str(int(r))
			n_in10=(n_in10-r)/b
		return n_in_b[::-1]


	print(n_from_a_to_b(n,a,b))

